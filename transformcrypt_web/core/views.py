import os
import json
import csv
import io
import sys

# Adjust the path to locate encryption module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from encryption_module import encrypt, decrypt

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def home(request):
    context = {}

    if request.method == "POST":
        input_text = request.POST.get("text")
        uploaded_file = request.FILES.get("file")

        # === FILE HANDLING ===
        if uploaded_file:
            file_name, file_ext = os.path.splitext(uploaded_file.name.lower())

            if file_ext not in [".txt", ".csv", ".json", ".enc"]:
                context["error"] = "Only .txt, .csv, .json, and .enc files are supported."
                return render(request, "home.html", context)

            # Read stream safely
            raw_bytes = uploaded_file.read()
            try:
                file_text = raw_bytes.decode("utf-8")
            except UnicodeDecodeError:
                context["error"] = "File must be in UTF-8 format."
                return render(request, "home.html", context)

            # Encrypt or decrypt logic
            if "encrypt" in request.POST:
                result = encrypt(file_text)
                download_name = f"{file_name}.enc"
                success_message = "✅ File encrypted successfully."

            elif "decrypt" in request.POST:
                try:
                    result = decrypt(file_text)
                    download_name = f"{file_name}_decrypted.txt"
                    success_message = "✅ File decrypted successfully."
                except Exception as e:
                    context["error"] = f"Decryption failed: {str(e)}"
                    return render(request, "home.html", context)

            # Stream output back to user
            response = HttpResponse(result, content_type="text/plain")
            response["Content-Disposition"] = f'attachment; filename="{download_name}"'
            return response

        # === TEXT HANDLING ===
        if input_text:
            if "encrypt" in request.POST:
                context["output"] = encrypt(input_text)
            elif "decrypt" in request.POST:
                try:
                    context["output"] = decrypt(input_text)
                except Exception as e:
                    context["error"] = f"Decryption failed: {str(e)}"

    return render(request, "home.html", context)
