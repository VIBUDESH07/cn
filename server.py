# WebSocket server for numeric conversion
import asyncio
import websockets

# Function to convert decimal to binary
def decimal_to_binary(num):
    return bin(num).replace("0b", "")

# Function to convert decimal to octal
def decimal_to_octal(num):
    return oct(num).replace("0o", "")

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(num):
    return hex(num).replace("0x", "")

# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Function to convert octal to decimal
def octal_to_decimal(octal_str):
    return int(octal_str, 8)

# Function to convert hexadecimal to decimal
def hexadecimal_to_decimal(hex_str):
    return int(hex_str, 16)

# Handling incoming client requests
async def conversion_handler(websocket, path):
    async for message in websocket:
        # Message should be of the format: conversion_type,value
        conversion_type, value = message.split(',')
        
        if conversion_type == "decimal_to_binary":
            result = decimal_to_binary(int(value))
        elif conversion_type == "decimal_to_octal":
            result = decimal_to_octal(int(value))
        elif conversion_type == "decimal_to_hexadecimal":
            result = decimal_to_hexadecimal(int(value))
        elif conversion_type == "binary_to_decimal":
            result = str(binary_to_decimal(value))
        elif conversion_type == "octal_to_decimal":
            result = str(octal_to_decimal(value))
        elif conversion_type == "hexadecimal_to_decimal":
            result = str(hexadecimal_to_decimal(value))
        else:
            result = "Invalid conversion type!"
        
        await websocket.send(result)

# Main server function
async def main():
    async with websockets.serve(conversion_handler, "localhost", 8765):
        print("WebSocket server is running on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
