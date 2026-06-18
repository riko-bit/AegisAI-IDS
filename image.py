from PIL import Image, ImageDraw, ImageFont

width, height = 900, 900
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

font = ImageFont.load_default()

boxes = [
    "Network Traffic",
    "Packet Capture (PyShark / TShark)",
    "Feature Extraction (Packet Length, Protocol)",
    "Feature Scaling (StandardScaler)",
    "Anomaly Detection (Autoencoder)",
    "Attack Classification (Random Forest)",
    "Alert Manager (API Request)",
    "FastAPI Backend",
    "Dashboard / Monitoring"
]

box_width = 520
box_height = 60
start_x = (width - box_width) // 2
y = 40

centers = []

for text in boxes:
    draw.rectangle([start_x, y, start_x + box_width, y + box_height], outline="black", width=2)
    bbox = draw.textbbox((0,0), text, font=font)
    w = bbox[2]-bbox[0]
    h = bbox[3]-bbox[1]
    draw.text((start_x + (box_width-w)/2, y + (box_height-h)/2), text, fill="black", font=font)
    centers.append((start_x + box_width//2, y + box_height))
    y += 90

for i in range(len(centers)-1):
    x1,y1 = centers[i]
    x2 = centers[i+1][0]
    y2 = centers[i+1][1] - box_height
    draw.line((x1,y1,x2,y2), fill="black", width=2)
    draw.polygon([(x2-5,y2-5),(x2+5,y2-5),(x2,y2)], fill="black")

path = "architecture/ai_ids_system_architecture.png"
img.save(path)

path