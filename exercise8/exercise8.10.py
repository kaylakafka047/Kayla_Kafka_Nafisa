def send_messages(messages, sent_messages):
    """Mencetak pesan dan memindahkannya ke list sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

messages = ["Pesan 1: Halo", "Pesan 2: Selamat pagi", "Pesan 3: Semangat belajar"]
sent_messages = []

send_messages(messages, sent_messages)

print("\n--- Status List Akhir ---")
print(f"List asli (messages): {messages}")
print(f"List terkirim (sent_messages): {sent_messages}")