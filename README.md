# Faded's Webhook
A simple python websocket server. (no really.. it's just a websocket server.)

# Execution Code
I would recommend putting this in your autoexec. It should be undetectable by itself as it's just opening a local websocket.
```lua
local socket = WebSocket.connect("ws://localhost:6969")

socket.OnMessage:Connect(function(Msg)
    loadstring(Msg)() -- Execute script
end)
```
