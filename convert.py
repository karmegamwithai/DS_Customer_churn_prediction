import markdown

# Read markdown file
with open("Customer_Churn_Prediction.md", "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_text)

# Full HTML page
full_html = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Markdown to HTML</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Poppins Font -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>
        body {{
            font-family: 'Poppins', sans-serif;
        }}

        pre {{
            overflow-x: auto;
            border-radius: 12px;
            padding: 15px;
            background: #111827;
            color: white;
        }}

        code {{
            font-family: monospace;
        }}
    </style>
</head>

<body class="bg-gray-100 py-10">

<div class="max-w-5xl mx-auto bg-white shadow-2xl rounded-3xl p-10">

{html_content}

</div>

</body>
</html>
"""

# Save HTML
with open("output.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("HTML file created successfully!")