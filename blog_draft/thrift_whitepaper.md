# Thrift 论文笔记
翻译很难，摘抄还行。摘抄 + 精简。

Terminology::
1. IDL (interface definition language)


## abstract

Thrift is a software library and set of code-generation tools.

Its primary goal is to enable efficient and reliable communication across programming
languages by abstracting the portions(部分) of each language.

Specifically, thrift offers IDL and code generation.

## Introduction

Background::
1. LAMP framework is too limited
2. Facebook's engineering culture:
   - choosing the best tools and implementations
   - begrudgingly accepting its inherent limitations.
3. Existing solutions:
   - no sufficient datatype freedom (protobuf?)
   - suffering from subpar performance

Thrift::
1. Choosing static code generation over a dynamic system allows
us to create validated code.(thriftpy?)

Key Challenges::
- `Types`: Common type system -> corresponding to language native types.
- `Transport`: common interface to bidirectional raw data transport.
TCP stream sockets, raw data in memory, files on disk.
- `Protocol`: using the Transport layer to encode and decode datatypes.
- `Versioning`
- `Processors`: processing data streams to accomplish remote procedure calls.

## Types

The goal of the Thrift type system is to enable programmers to
develop using completely natively defined types.

### Base Types
bool, i8, i16, i32, i64, double, string.

No unsigned integers.

### Structs

Class / C Struct

### Containers
C++ template / Java Generices

- list\<type\> An ordered list of elements. Translates directly
into an STL `vector`, Java `ArrayList`, or native array in script-
ing languages. May contain duplicates.
- set\<type\> An unordered set of unique elements. Translates
into an STL `set`, Java `HashSet`, `set` in Python, or native
dictionary in PHP/Ruby.
- map<type1,type2> A map of strictly unique keys to values
Translates into an STL `map`, Java `HashMap`, PHP `associative
array`, or Python/Ruby dictionary.

Custom code generator directives have been added to substitute custom types
in destination languages. The only requirement is that the custom types
support all the necessary iteration primitives.

In the target language, each definition generates a type with two
methods, read and write, which perform serialization and trans-
port of the objects using a Thrift TProtocol object.

### Exceptions
Exceptions are syntactically and functionally equivalent to structs
except that they are declared using the exception keyword instead
of the struct keyword.

Again, the design emphasis is on making the code familiar
to the application developer.

### Services
Services are defined using Thrift types. Definition of a service is
semantically equivalent to defining an interface (or a pure virtual
abstract class) in object oriented programming.

## Transport
The transport layer is used by the generated code to facilitate data
transfer.

### Interface

A key design choice in the implementation of Thrift was to de-
couple the transport layer from the code generation layer.

Though Thrift is typically used on top of the TCP/IP stack with streaming
sockets as the base layer of communication, there was no compelling reason
to build that constraint into the system.

TTransport::
- `open` Opens the tranpsort
- `close` Closes the tranport
- `isOpen` Indicates whether the transport is open
- `read` Reads from the transport
- `write` Writes to the transport
- `flush` Forces any pending writes

TServerTransport::
- open Opens the transport
- listen Begins listening for connections
- accept Returns a new client transport
- close Closes the transport

### Implementation
#### TSocket
#### TFileTransport
#### Utilities
The Transport interface is designed to support easy extension us-
ing common OOP techniques, such as composition.

## protocol
Thrift enforces a certain messaging structure when transporting data.

### Interface
The Thrift Protocol interface is very straightforward. It fundamen-
tally supports two things::
1. bidirectional sequenced messaging
2. encoding of base types, containers, and structs

```
writeMessageBegin(name, type, seq)
writeMessageEnd()
writeStructBegin(name)
writeStructEnd()
writeFieldBegin(name, type, id)
writeFieldEnd()
writeFieldStop()
writeMapBegin(ktype, vtype, size)
writeMapEnd()
writeListBegin(etype, size)
writeListEnd()
writeSetBegin(etype, size)
writeSetEnd()
writeBool(bool)
writeByte(byte)
writeI16(i16)
writeI32(i32)
writeI64(i64)
writeDouble(double)
writeString(string)

name, type, seq = readMessageBegin()
readMessageEnd()
name = readStructBegin()
readStructEnd()
name, type, id = readFieldBegin()
readFieldEnd()
k, v, size = readMapBegin()
readMapEnd()
etype, size = readListBegin()
readListEnd()
etype, size = readSetBegin()
readSetEnd()
bool = readBool()
byte = readByte()
i16 = readI16()
i32 = readI32()
i64 = readI64()
double = readDouble()
string = readString()
```

- write -> writeFieldStop ---> writeStructEnd
- read => readFieldBegin -> stop field -> readStructEnd

### Structure
Thrift structures are designed to support encoding into a streaming
protocol. The implementation should never need to frame or com-
pute the entire data length of a structure prior to encoding it.

However, if the list can be written as **iteration** is
performed, the corresponding read may begin in parallel, theoreti-
cally offering an end-to-end speedup of (kN − C), where N is the
size of the list, k the cost factor associated with serializing a sin-
gle element, and C is fixed offset for the delay between data being
written and becoming available to read.

### Implementation
Facebook has implemented and deployed a space-efficient binary
protocol which is used by most backend services.

## Versioning
The system must be able to support reading of
old data from log files, as well as requests from out-of-date clients
to new servers, and vice versa.

### Field Identifiers(WIP)
The combination of this field identifier
and its type specifier is used to uniquely identify the field.
