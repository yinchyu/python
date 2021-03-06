// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.25.0
// 	protoc        v3.14.0
// source: receiver.proto

package proto

import (
	proto "github.com/golang/protobuf/proto"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	structpb "google.golang.org/protobuf/types/known/structpb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type Event struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Appid    string           `protobuf:"bytes,1,opt,name=appid,proto3" json:"appid,omitempty"`
	Xwhen    int32            `protobuf:"varint,2,opt,name=xwhen,proto3" json:"xwhen,omitempty"`
	Xwho     string           `protobuf:"bytes,3,opt,name=xwho,proto3" json:"xwho,omitempty"`
	Xwhat    string           `protobuf:"bytes,4,opt,name=xwhat,proto3" json:"xwhat,omitempty"`
	Xcontext *structpb.Struct `protobuf:"bytes,5,opt,name=xcontext,proto3" json:"xcontext,omitempty"`
}

func (x *Event) Reset() {
	*x = Event{}
	if protoimpl.UnsafeEnabled {
		mi := &file_receiver_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Event) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Event) ProtoMessage() {}

func (x *Event) ProtoReflect() protoreflect.Message {
	mi := &file_receiver_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Event.ProtoReflect.Descriptor instead.
func (*Event) Descriptor() ([]byte, []int) {
	return file_receiver_proto_rawDescGZIP(), []int{0}
}

func (x *Event) GetAppid() string {
	if x != nil {
		return x.Appid
	}
	return ""
}

func (x *Event) GetXwhen() int32 {
	if x != nil {
		return x.Xwhen
	}
	return 0
}

func (x *Event) GetXwho() string {
	if x != nil {
		return x.Xwho
	}
	return ""
}

func (x *Event) GetXwhat() string {
	if x != nil {
		return x.Xwhat
	}
	return ""
}

func (x *Event) GetXcontext() *structpb.Struct {
	if x != nil {
		return x.Xcontext
	}
	return nil
}

type Reply struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Status  int32  `protobuf:"varint,1,opt,name=status,proto3" json:"status,omitempty"`
	Message string `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
}

func (x *Reply) Reset() {
	*x = Reply{}
	if protoimpl.UnsafeEnabled {
		mi := &file_receiver_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Reply) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Reply) ProtoMessage() {}

func (x *Reply) ProtoReflect() protoreflect.Message {
	mi := &file_receiver_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Reply.ProtoReflect.Descriptor instead.
func (*Reply) Descriptor() ([]byte, []int) {
	return file_receiver_proto_rawDescGZIP(), []int{1}
}

func (x *Reply) GetStatus() int32 {
	if x != nil {
		return x.Status
	}
	return 0
}

func (x *Reply) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

var File_receiver_proto protoreflect.FileDescriptor

var file_receiver_proto_rawDesc = []byte{
	0x0a, 0x0e, 0x72, 0x65, 0x63, 0x65, 0x69, 0x76, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2f, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x92,
	0x01, 0x0a, 0x05, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x14, 0x0a, 0x05, 0x61, 0x70, 0x70, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x61, 0x70, 0x70, 0x69, 0x64, 0x12, 0x14,
	0x0a, 0x05, 0x78, 0x77, 0x68, 0x65, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x05, 0x78,
	0x77, 0x68, 0x65, 0x6e, 0x12, 0x12, 0x0a, 0x04, 0x78, 0x77, 0x68, 0x6f, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x04, 0x78, 0x77, 0x68, 0x6f, 0x12, 0x14, 0x0a, 0x05, 0x78, 0x77, 0x68, 0x61,
	0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x78, 0x77, 0x68, 0x61, 0x74, 0x12, 0x33,
	0x0a, 0x08, 0x78, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x08, 0x78, 0x63, 0x6f, 0x6e, 0x74,
	0x65, 0x78, 0x74, 0x22, 0x39, 0x0a, 0x05, 0x52, 0x65, 0x70, 0x6c, 0x79, 0x12, 0x16, 0x0a, 0x06,
	0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x06, 0x73, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x32, 0x45,
	0x0a, 0x08, 0x52, 0x65, 0x63, 0x65, 0x69, 0x76, 0x65, 0x72, 0x12, 0x1b, 0x0a, 0x07, 0x72, 0x65,
	0x63, 0x65, 0x69, 0x76, 0x65, 0x12, 0x06, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x1a, 0x06, 0x2e,
	0x52, 0x65, 0x70, 0x6c, 0x79, 0x22, 0x00, 0x12, 0x1c, 0x0a, 0x08, 0x72, 0x65, 0x63, 0x65, 0x69,
	0x76, 0x65, 0x32, 0x12, 0x06, 0x2e, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x1a, 0x06, 0x2e, 0x52, 0x65,
	0x70, 0x6c, 0x79, 0x22, 0x00, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_receiver_proto_rawDescOnce sync.Once
	file_receiver_proto_rawDescData = file_receiver_proto_rawDesc
)

func file_receiver_proto_rawDescGZIP() []byte {
	file_receiver_proto_rawDescOnce.Do(func() {
		file_receiver_proto_rawDescData = protoimpl.X.CompressGZIP(file_receiver_proto_rawDescData)
	})
	return file_receiver_proto_rawDescData
}

var file_receiver_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_receiver_proto_goTypes = []interface{}{
	(*Event)(nil),           // 0: Event
	(*Reply)(nil),           // 1: Reply
	(*structpb.Struct)(nil), // 2: google.protobuf.Struct
}
var file_receiver_proto_depIdxs = []int32{
	2, // 0: Event.xcontext:type_name -> google.protobuf.Struct
	0, // 1: Receiver.receive:input_type -> Event
	0, // 2: Receiver.receive2:input_type -> Event
	1, // 3: Receiver.receive:output_type -> Reply
	1, // 4: Receiver.receive2:output_type -> Reply
	3, // [3:5] is the sub-list for method output_type
	1, // [1:3] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_receiver_proto_init() }
func file_receiver_proto_init() {
	if File_receiver_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_receiver_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Event); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_receiver_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Reply); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_receiver_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_receiver_proto_goTypes,
		DependencyIndexes: file_receiver_proto_depIdxs,
		MessageInfos:      file_receiver_proto_msgTypes,
	}.Build()
	File_receiver_proto = out.File
	file_receiver_proto_rawDesc = nil
	file_receiver_proto_goTypes = nil
	file_receiver_proto_depIdxs = nil
}
