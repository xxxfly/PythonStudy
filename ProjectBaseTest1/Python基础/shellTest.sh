addStrs(){
    str=$1
    if [ -z ${strs[0]} ]
    then
        strs[0]=$str
    fi
    echo "str:$str"
    index=0
    for item in ${strs[@]}
    do
        if [ $str = $item ]
        then
            echo "true"
            if [ -z ${result[$index]} ]
            then
                result[$index]=0
            else
                result[$index]=${result[$index]}
            fi
            result[$index]=`expr ${result[$index]} + 1`
            break
        else
            echo "false"
            strs[$index]=$str
        fi
        index=`expr $index + 1`
    done
    echo "index:$index"
    echo "strs ${strs[@]}"
   # echo "result ${result[@]}"
}



# 字典
# 必须先声明
declare -A dic
dic=(["a"]=1 ["b"]="2" [c]=3)

# 获取key 的值
echo "a:" ${dic["a"]}
echo "b:" ${dic["b"]}
echo "c:" ${dic["c"]}

# 获取所有的key
echo "key:" ${!dic[*]}

# 获取所有的value
echo "value:" ${dic[*]}

# 添加一个新元素
dic+=(["d"]="4")

# 遍历key值
for key in $(echo ${!dic[*]})
do
    echo "$key:${dic[$key]}"
done
