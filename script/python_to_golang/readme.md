# python 调用 go

go 性能性能强
python 丰富的社区
两种语言各具特点，结合使用可以起到优势的互补

go ：计算 30 的斐波那契值需要 0.003725s
python ：计算 30 的斐波那契值需要 0.21982765197753906s

将 go 代码生成动态链库：命令：
go build -buildmode=c-shared -o 生成的 so 文件名 (main.so) 构建的 go 文件(go.go)

python 中调用动态链接库
