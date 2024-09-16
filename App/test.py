from pyngrok import ngrok

# Authenticate ngrok with your token
ngrok.set_auth_token("2jyPjTw7h9wpilF6elqaDHreoMG_7bsfDDyCQZCML3NdKdbvh")

# Start ngrok tunnel on port 5000 with the reserved domain
http_tunnel = ngrok.connect(5000, subdomain="suited-unbiased-drake")

# Get the public URL of the tunnel
public_url = http_tunnel.public_url
print(f"ngrok tunnel -> {public_url}")

# Keep the script running to maintain the ngrok tunnel
try:
    input("Press Ctrl+C to exit...\n\n")
except KeyboardInterrupt:
    print("Shutting down ngrok tunnel...")

ngrok.kill()
