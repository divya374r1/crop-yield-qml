document.addEventListener("DOMContentLoaded", () => {

    const ctx = document.getElementById("yieldChart");

    if (!ctx) return;

    const mlYield = parseFloat(ctx.dataset.ml);
    const qmlYield = parseFloat(ctx.dataset.qml);

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Classical ML", "Quantum ML"],
            datasets: [{
                label: "Predicted Yield",
                data: [mlYield, qmlYield],
                backgroundColor: ["#2563eb", "#16a34a"],
                borderRadius: 10
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

});
