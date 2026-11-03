def send_messages(messages, sent_messages):
    """Mencetak pesan dan memindahkannya ke list sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim salinan pesan: {current_message}")
        sent_messages.append(current_message)

messages = ["Pesan A", "Pesan B", "Pesan C"]
sent_messages = []

# Mengirim salinan list menggunakan slice [:]
send_messages(messages[:], sent_messages)

print("\n--- Pemeriksaan Arsip List Asli ---")
print(f"List asli (messages) tetap utuh: {messages}")
print(f"List terkirim (sent_messages): {sent_messages}")