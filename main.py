from pyscript import document

def calculate_gwa(event):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    
    science = float(document.getElementById("science").value or 0)
    math = float(document.getElementById("math").value or 0)
    english = float(document.getElementById("english").value or 0)
    filipino = float(document.getElementById("filipino").value or 0)
    ict = float(document.getElementById("ict").value or 0)
    pe = float(document.getElementById("pe").value or 0)

    grades = [science, math, english, filipino, ict, pe]
    units = [3, 3, 3, 3, 3, 2]

    
    total = 0
    total_units = 0
    for grade, unit in zip(grades, units):
        total += grade * unit
        total_units += unit

    gwa = total / total_units

   
    if gwa > 74:
        status = "PASSED"
    else:
        status = "FAILED"

 
    result_div = document.getElementById("result")
    result_div.innerHTML = f"""
        Student: {fname} {lname}<br>
        <b>GWA:</b> {gwa:.2f}<br>
        <b>Status:</b> {status}
    """