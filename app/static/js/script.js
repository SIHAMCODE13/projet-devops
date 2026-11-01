// Rafraîchit automatiquement l'état du service toutes les 5 secondes.
const REFRESH_MS = 5000;

async function refreshHealth() {
    const badge = document.getElementById("status");
    try {
        const response = await fetch("/api/health", { cache: "no-store" });
        if (!response.ok) throw new Error("HTTP " + response.status);
        const data = await response.json();

        document.getElementById("service").textContent = data.service;
        document.getElementById("version").textContent = data.version;
        document.getElementById("uptime").textContent = data.uptime_seconds;
        badge.textContent = data.status;
        badge.className = "badge " + (data.status === "UP" ? "up" : "down");
    } catch (error) {
        badge.textContent = "DOWN";
        badge.className = "badge down";
    }
    document.getElementById("last-check").textContent = new Date().toLocaleTimeString();
}

refreshHealth();
setInterval(refreshHealth, REFRESH_MS);
