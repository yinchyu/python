
package main

import (
	"context"
	"google.golang.org/grpc"
	"log"
	pb "main/proto"
	"net"
)

// 实现 GetSimpleInfo 方法
// 继承之后重写方法就可以操作，但是有一个包的问题没有解决，不知道怎么操作
type  receiver struct {
	pb.UnimplementedReceiverServer

}
func (s *receiver) Receive(ctx context.Context, req *pb.Event) (*pb.Reply, error) {
	data := req
	log.Println("get from client: ", data)
	resp := &pb.Reply{
	Status:  8888,
	Message: "receive1",
	}
	return resp, nil
}
func (s *receiver) Receive2(ctx context.Context, req *pb.Event) (*pb.Reply, error){
	data := req
	log.Println("get from client: ", data)
	resp := &pb.Reply{
		Status:  0000,
		Message: "receive2",
	}
	return resp, nil
}

// 调用grpc 简单请求
func display() {
	// 1.监听端口
	listener, err := net.Listen(Network, Address)
	if err != nil {
		log.Fatalf("net.listen err: %v", err)
	}
	log.Println(Address, " net listening...")
	// 2.实例化gRPC服务端
	grpcServer := grpc.NewServer()
	pb.RegisterReceiverServer(grpcServer,&receiver{})
	// 4.启动gRPC服务端
	err = grpcServer.Serve(listener)
	if err != nil {
		log.Fatalf("grpc server err: %v", err)
	}
}

