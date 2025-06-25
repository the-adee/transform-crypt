import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from encryption_module import encrypt, decrypt


from django.shortcuts import render

def home(request):
    result = ""
    input_text = ""
    error = ""

    if request.method == "POST":
        input_text = request.POST.get("text")
        if "encrypt" in request.POST:
            result = encrypt(input_text)
        elif "decrypt" in request.POST:
            try:
                result = decrypt(input_text)
            except Exception:
                error = "⚠️ Decryption failed: Please make sure you're pasting a valid encrypted string."

    return render(request, "home.html", {
        "input": input_text,
        "output": result,
        "error": error,
    })
