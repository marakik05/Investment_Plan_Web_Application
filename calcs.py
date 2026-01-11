from flask import Flask, request, jsonify,render_template
from file_handler import safe_float;

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/calculate", methods=["POST"])




def calculate_sum(): 
    data = request.get_json()
    
    young = data.get("young", False)
    esdim = data.get("esdim", False)
   
    district = data.get("district", "")
    invest_type = data.get("invest_type", "")  
    raw_costs = data.get("costs", [])
    categories = data.get("categories", [])
    turnover = safe_float(data.get("turnover"))

    costs = []
    valid_pairs = []
    messages = []

    if turnover <= 0:
        messages.append("Ο κύκλος εργασιών πρέπει να είναι θετικός αριθμός.")
    
    for i, (category, cost) in enumerate(zip(categories, raw_costs)):
        cost_value = safe_float(cost)

        if not category:
            messages.append(f"Η κατηγορία δαπάνης #{i+1} δεν έχει επιλεγεί.")
            continue

        if cost_value <= 0:
            messages.append(f"Το ποσό δαπάνης #{i+1} πρέπει να είναι θετικό.")
            continue

        valid_pairs.append((category, cost_value))
        costs.append(cost_value)


    island=district in ["Νότιο Αιγαίο", "Βόρειο Αιγαίο"]
    idia_values=[]
    
    
    for category, cost in valid_pairs:
        
        
        if not young :
            if esdim:
                if island:
                    if category in [
                        "Γεωργικοί ελκυστήρες, περονοφόροι φορτωτές & bobcat",
                        "Λοιπές δαπάνες"
                    ]:
                        rate = 0.6
                    else:
                        rate = 0.7
                else:
                    if category in [
                        "Γεωργικοί ελκυστήρες, περονοφόροι φορτωτές & bobcat",
                        "Λοιπές δαπάνες"
                    ]:
                        rate = 0.5
                    elif category in ["ΑΠΕ", "Εξοικονόμηση Ύδατος"]:
                        rate = 0.7
                    else:
                        rate = 0.65
            else:
                if island:
                    if category in [
                        "Γεωργικοί ελκυστήρες, περονοφόροι φορτωτές & bobcat",
                        "Λοιπές δαπάνες"
                    ]:
                        rate = 0.6
                    else:
                        rate = 0.7
                else:
                    if category in [
                        "Γεωργικοί ελκυστήρες, περονοφόροι φορτωτές & bobcat",
                        "Λοιπές δαπάνες"
                    ]:
                        rate = 0.5
                    elif category in ["ΑΠΕ", "Εξοικονόμηση Ύδατος"]:
                        rate = 0.7
                    else:
                        rate = 0.6 
        else:
            if category in [
            "Γεωργικοί ελκυστήρες, περονοφόροι φορτωτές & bobcat",
            "Λοιπές δαπάνες"] :
                rate = 0.6 
            else:
                rate = 0.7

        idia_values.append(cost * rate)
                

   

    total_budget = sum(costs)
    idia=sum(idia_values)     

    idia_30 = idia * 0.3
   

  

    if turnover < idia_30:
        messages.append("Μη επιλέξιμος προϋπολογισμός λόγω χαμηλού κύκλου εργασιών.")

    if invest_type == "Επενδύσεις ΑΠΕ" and total_budget > 200000:
        messages.append("Μη επιλέξιμος προϋπολογισμός για Επενδύσεις ΑΠΕ άνω των 200.000€.")
    
    if invest_type == "Επενδύσεις Παραγωγής Βιοαερίου" and total_budget > 2500000:
        messages.append("Μη επιλέξιμος προϋπολογισμός για Επενδύσεις Παραγωγής Βιοαερίου άνω των 2.500.000€.")

    if invest_type == "Επενδύσεις Εξοικονόμηση Ύδατος" and total_budget > 150000:
        messages.append("Μη επιλέξιμος προϋπολογισμός για Επενδύσεις Εξοικονόμηση Ύδατος άνω των 150.000€.")    
    
    if invest_type == "Λοιπές επενδύσεις φυτικής παραγωγής, μελισσοκομίας, σηροτροφία" and total_budget > 200000:
        messages.append("Μη επιλέξιμος προϋπολογισμός για Λοιπές επενδύσεις φυτικής παραγωγής, μελισσοκομίας, σηροτροφία άνω των 200.000€.")

    if invest_type == "Λοιπές επενδύσεις ζωικής παραγωγή" and total_budget > 400000:
        messages.append("Μη επιλέξιμος προϋπολογισμός για Λοιπές επενδύσεις ζωικής παραγωγή άνω των 400.000€.")    


   

    return jsonify({
        "status": "error" if messages else "success",
        "budget": total_budget,
        "idia": idia,
        "idia_30": idia_30,
        "messages": messages
    })

if __name__ == "__main__":
    app.run(debug=True)

