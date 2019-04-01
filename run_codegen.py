"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""
from grpc_tools import protoc

#grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/example.proto

protoc.main((
    '',
    '-I./protos',
    '--python_out=.',
    '--grpc_python_out=.',
    './protos/pingpong.proto',
))
