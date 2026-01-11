// Εισαγωγή μόνο θετικών ακέραιων αριθμών και μίας τελείας στα number inputs
document.addEventListener("input", function (e) {

  if (
    e.target.matches('input[name="cost[]"], input[name="turnover"]')
  ) {
    let value = e.target.value;

    // ❌ όχι κόμμα
    value = value.replace(/,/g, "");

    // ❌ όχι αρνητικά
    value = value.replace(/-/g, "");

    // ❌ μόνο αριθμοί και τελεία
    value = value.replace(/[^0-9.]/g, "");

    // ❌ μόνο ΜΙΑ τελεία
    const firstDot = value.indexOf(".");
    if (firstDot !== -1) {
      value =
        value.slice(0, firstDot + 1) +
        value.slice(firstDot + 1).replace(/\./g, "");
    }

    e.target.value = value;
  }
});

 
 // Προσθήκη νέου πεδίου δαπάνης
 document.getElementById("add-expense").addEventListener("click", function () {
                    const container = document.getElementById("expenses-container");
                    const fieldset = container.querySelector(".expense-fieldset");

                    const clone = fieldset.cloneNode(true);

                    
// Καθαρισμός πεδίων
                    clone.querySelectorAll("input").forEach(input => input.value = "");
                    clone.querySelectorAll("select").forEach(select => select.selectedIndex = 0);


                     // εμφάνιση remove button
                    const removeBtn = clone.querySelector(".remove-expense");
                    removeBtn.classList.remove("hidden");

                    container.appendChild(clone);
 });




// Event delegation για αφαίρεση
                document.getElementById("expenses-container").addEventListener("click", function (e) {
                    if (e.target.classList.contains("remove-expense")) {
                        e.target.closest(".expense-fieldset").remove();
                    }
                });
  document.getElementById("calc-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const messageBox = document.getElementById("form-message");
    messageBox.style.display = "none";
    messageBox.className = "form-message";
    messageBox.innerHTML = "";

   

                    // ✔ costs
                    const costInputs = document.querySelectorAll('input[name="cost[]"]');
                    const costs = [];
                    costInputs.forEach(input => {
                        const value = parseFloat(input.value);
                        if (!isNaN(value)) costs.push(value);
                    });

                    // ✔ categories
                    const categorySelects = document.querySelectorAll('select[name="category[]"]');
                    const categories = [];
                    categorySelects.forEach(select => {
                        if (select.value !== "--Επιλέξτε") {
                            categories.push(select.value);
                        }
                    });

                    // ✔ checkbox
                    const young = document.getElementById("young").checked;
                    const esdim = document.getElementById("esdim").checked;

                    // ✔ αριθμός
                    const turnover = parseFloat(document.getElementById("turnover").value) || 0;

                    // ✔ select
                    const district = document.getElementById("district").value;

                    // ✔ radio
                    const investType = document.querySelector('input[name="invest_type"]:checked')?.id;

                   
                        const payload = {
                            costs,
                            categories,
                            young,
                            esdim,
                            turnover,
                            district,
                            invest_type: investType
                        };
                    

        const response = await fetch("/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

        const result = await response.json();
        
        document.getElementById("budget").value = result.budget;
        document.getElementById("idia").value = result.idia;
        document.getElementById("30_idia").value = result.idia_30;

   if (result.messages && result.messages.length > 0) {
    messageBox.innerHTML = result.messages.join("<br>");
    messageBox.classList.add("error");
    messageBox.style.display = "block";
} else {
    messageBox.textContent = "Επιλέξιμος προϋπολογισμός-Ο υπολογισμός ολοκληρώθηκε επιτυχώς. ";
    messageBox.classList.add("success");
    messageBox.style.display = "block";
}
    });
           
