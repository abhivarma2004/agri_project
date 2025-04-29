document.getElementById("searchInput").addEventListener("input", async function () {
    const query = this.value.toLowerCase().trim();
    const cropInfoDiv = document.getElementById("cropInfo");
  
    if (query.length === 0) {
      cropInfoDiv.classList.add("hidden");
      return;
    }
  
    try {
      const response = await fetch("../data/crops.json");
      const crops = await response.json();
  
      if (crops[query]) {
        const crop = crops[query];
        document.getElementById("cropName").innerText = query.charAt(0).toUpperCase() + query.slice(1);
        document.getElementById("season").innerText = crop.season;
        document.getElementById("soil").innerText = crop.soil;
        document.getElementById("climate").innerText = crop.climate;
        document.getElementById("fertilizer").innerText = crop.fertilizer;
        document.getElementById("harvest").innerText = crop.harvest;
        cropInfoDiv.classList.remove("hidden");
      } else {
        cropInfoDiv.classList.add("hidden");
      }
    } catch (err) {
      console.error("Error loading crop data:", err);
    }
  });
  