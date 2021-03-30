
# python 调用go

go性能性能强
python丰富的社区
两种语言各具特点，结合使用可以起到优势的互补


go ：计算30的斐波那契值需要0.003725s
python ：计算30的斐波那契值需要0.21982765197753906s

将go代码生成动态链库：命令：
go build -buildmode=c-shared -o  生成的so文件名 (main.so) 构建的go文件(go.go)

python中调用动态链接库