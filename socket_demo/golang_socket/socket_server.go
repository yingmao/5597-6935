package main
import (
        "fmt"
        "net"
        "os"
)

const (
        SERVER_HOST = "localhost"
        SERVER_PORT = "9988"
        SERVER_TYPE = "tcp"
)

func main() {
        fmt.Println("Server Running...")
        // listening port，start socket server
        server, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
        if err != nil {
                fmt.Println("Error listening:", err.Error())
                os.Exit(1)
        }
        // close socket
        defer server.Close()
        fmt.Println("Listening on " + SERVER_HOST + ":" + SERVER_PORT)
        fmt.Println("Waiting for client...")
        for {
                connection, err := server.Accept()
                if err != nil {
                        fmt.Println("Error accepting: ", err.Error())
                        os.Exit(1)
                }
                fmt.Println("client connected")

                buffer := make([]byte, 1024)
                mLen, err := connection.Read(buffer)
                if err != nil {
                    fmt.Println("Error reading:", err.Error())
                }
                fmt.Println("Received: ", string(buffer[:mLen]))
                _, err = connection.Write([]byte("Thanks! Got your message:" + string(buffer[:mLen])))
                connection.Close()

                // TODO：multi-threading
                // go processClient(connection)
        }
}
