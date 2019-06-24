<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="UpdateVideo.aspx.cs" Inherits="FL.Hall.HWWeb720p.Home.UpdateVideo" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>修改工单信息</title>
    <link href="../include/bootstrap-3.3.7-dist/css/bootstrap.min.css" rel="Stylesheet" />
    <style type="text/css">
        a:
        {
            cursor: pointer;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div class="container-fluid" id="pageData">
        <div class="row" style="padding-top: 30px; padding-bottom: 20px;">
            <div class="col-md-3">
                <select class="form-control" v-model="pageAction.selectedStatus" v-on:change="selectChange('status')">
                    <option value="000">选择状态</option>
                    <option value="0">未注入</option>
                    <option value="1">注入中</option>
                    <option value="2">注入成功</option>
                    <option value="3">注入失败</option>
                    <option value="5">删除成功</option>
                    <option value="6">删除失败</option>
                    <option value="8">修改成功</option>
                    <option value="9">修改失败</option>
                    <option value="000">所有</option>
                </select>
            </div>
            <div class="col-md-3">
                <select class="form-control" v-model="pageAction.selectedType" v-on:change="selectChange('type')">
                    <option value="000">选择工单类型</option>
                    <option value="movie">电影</option>
                    <option value="series">剧头</option>
                    <option value="episode">剧集</option>
                    <option value="000">所有</option>
                </select>
            </div>
            <div class="col-md-3">
                <form>
                </form>
                <form class="form-inline pull-right">
                <div class="form-group">
                    <input type="text" class="form-control" id="Text1" placeholder="媒资ID" v-model="pageAction.searchProgramID">
                </div>
                <button type="button" id="btnProgram" class="btn btn-default" v-on:click="toSearch('program')">
                    媒资ID</button>
                </form>
            </div>
            <div class="col-md-3">
                <form class="form-inline pull-right">
                <div class="form-group">
                    <input type="text" class="form-control" id="videoName" placeholder="视频名称或编号" v-model="pageAction.searchVideoName">
                </div>
                <button type="button" id="btnVideo" class="btn btn-default" v-on:click="toSearch('video')">
                    搜索名称</button>
                </form>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        数据 共 {{totalCount}} 条 {{pageCount}}页</div>
                    <div class="panel-body">
                        <table class="table table-striped table-bordered table-hover table-responsive">
                            <thead>
                                <tr>
                                    <th class="text-center" style="width: 60px;" v-on:click="trCheckBoxAll">
                                        <a>
                                            <img src="../images/icon/checkbox-1.png" v-if="checkboxAll" />
                                            <img src="../images/icon/checkbox-0.png" v-else />
                                    </th>
                                    <th>
                                        媒资ID
                                    </th>
                                    <th>
                                        视频集ID
                                    </th>
                                    <th>
                                        内容名称
                                    </th>
                                    <th>
                                        FTP地址
                                    </th>
                                    <th>
                                        视频资源地址
                                    </th>
                                    <th>
                                        状态
                                    </th>
                                    <th>
                                        错误描述
                                    </th>
                                    <th>
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in data" v-bind:key="item.c_ProgramID">
                                    <th class="text-center" style="width: 60px;" v-on:click="trCheckBox(item.c_ProgramID)">
                                        <a>
                                            <img src="../images/icon/checkbox-1.png" v-if="checkboxList.indexOf(item.c_ProgramID)>-1" />
                                            <img src="../images/icon/checkbox-0.png" v-else />
                                        </a>
                                    </th>
                                    <th>
                                        {{ item.c_ProgramID }}
                                    </th>
                                    <th>
                                        {{ item.c_ResourceID }}
                                    </th>
                                    <th>
                                        {{ item.c_VideoName }}
                                    </th>
                                    <th>
                                        {{ item.c_XMLFtpUrl }}
                                    </th>
                                    <th>
                                        {{ item.c_FileURL }}
                                    </th>
                                    <th>
                                        {{ item.c_Status }}
                                    </th>
                                    <th>
                                        {{ item.c_ErrorDes }}
                                    </th>
                                    <th>
                                        <button type="button" id="Button2" class="btn btn-default btn-sm" style="margin: 4px;"
                                            v-on:click="showPop('show',item.c_ProgramID)">
                                            查看</button>
                                        <button type="button" id="Button3" class="btn btn-info btn-sm" style="margin: 4px;"
                                            v-on:click="showPop('update',item.c_ProgramID)">
                                            编辑</button>
                                        <button type="button" id="Button4" class="btn btn-danger btn-sm" style="margin: 4px;">
                                            删除</button>
                                    </th>
                                </tr>
                            </tbody>
                        </table>
                        <div class="row">
                            <div class="col-md-12">
                                <div class="pull-left" style="display: inline-block; padding-top: 20px;">
                                    <button type="button" id="Button11" class="btn btn-default" v-on:click="btnUploadFile">
                                        上传数据</button>
                                    <button type="button" id="Button12" class="btn btn-info" v-on:click="btnInsertXml">
                                        工单注入</button>
                                </div>
                                <form class="form-inline pull-right" style="display: inline-block; padding-top: 20px;
                                padding-left: 10px;">
                                <div class="form-group">
                                    <input type="number" class="form-control" style="width: 60px;" v-model="pageAction.toPageIndex">
                                    页
                                </div>
                                <button type="button" id="Button1" class="btn btn-default" v-on:click="toPage('toPage',0)">
                                    跳转</button>
                                </form>
                                <ul class="pagination pull-right">
                                    <li><a href="#" aria-label="FirstPage" v-on:click="toPage('FirstPage',0)"><span aria-hidden="true">
                                        第一页</span> </a></li>
                                    <li><a href="#" aria-label="Previous"><span aria-hidden="true" v-on:click="toPage('Previous',0)">
                                        上一页</span> </a></li>
                                    <li v-for="item in pageNumberList"><a v-on:click="toPage('number',item)" v-if="item==page.pageIndex"
                                        v-bind:style="{backgroundColor:'#ccc'}">{{item}}</a> <a v-on:click="toPage('number',item)"
                                            v-else>{{item}}</a> </li>
                                    <li><a href="#" aria-label="Next"><span aria-hidden="true" v-on:click="toPage('Next',0)">
                                        下一页</span> </a></li>
                                    <li><a href="#" aria-label="LastPage"><span aria-hidden="true" v-on:click="toPage('LastPage',0)">
                                        最后一页</span> </a></li>
                                </ul>
                                <div class="pull-right" style="display: inline-block; padding-top: 20px; padding-right: 10px;">
                                    <select class="form-control " v-model="pageAction.selectedPageSize" v-on:change="selectChange('pageSize')">
                                        <option value="20">选择分页大小</option>
                                        <option value="10">10</option>
                                        <option value="20">20</option>
                                        <option value="30">30</option>
                                        <option value="50">50</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <%--    查看内容--%>
        <div class="modal fade" id="showModalLabel" tabindex="-1" role="dialog" aria-labelledby="showModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                            &times;</button>
                        <h4 class="modal-title" id="myModalLabel">
                            查看内容</h4>
                    </div>
                    <div class="modal-body">
                        在这里添加一些文本</div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">
                            关闭</button>
                        <button type="button" class="btn btn-primary">
                            提交更改</button>
                    </div>
                </div>
            </div>
        </div>
        <%--    修改内容--%>
        <div class="modal fade" id="updateModalLabel" tabindex="-1" role="dialog" aria-labelledby="updateModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                            &times;</button>
                        <h4 class="modal-title" id="H1">
                            修改内容</h4>
                    </div>
                    <div class="modal-body">
                        在这里添加一些文本</div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">
                            关闭</button>
                        <button type="button" class="btn btn-primary">
                            提交更改</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </form>
    <script src="../include/jquery-3.2.1/jquery-3.2.1.min.js" type="text/javascript"></script>
    <script src="../include/bootstrap-3.3.7-dist/js/bootstrap.min.js" type="text/javascript"></script>
    <script src="../include/vue.js" type="text/javascript"></script>
    <script type="text/javascript">
        // 获取数据api
        url_getdata = "../Api/v1/GetVideoByPage.ashx";

        // 分页对象
        var pagination = {
            pageSize: 20,    //分页大小
            pageIndex: 1,    //当前页，从1开始          
            dropCondition: [],   //下拉选择条件
            searchCondition: [] //搜索条件
        }

        var vuePage = new Vue({
            el: "#pageData",
            data: {
                page: pagination, // 传递数据接口的风分页对象
                totalCount: 0,  // 数据总数
                pageCount: 0,    //分页数量
                data: [], // 数据列表
                pageNumberList:[1], // 数据页码展示列表
                checkboxList:[], // 数据选择列表
                checkboxAll:false,
                pageAction:{  
                    selectedStatus:"000",
                    selectedType: "000",
                    searchProgramID:null,
                    searchVideoName:null,
                    selectedPageSize:20,
                    toPageIndex:1,
                }
            },
            created:function(){
                var self=this;

                self.page.dropCondition.push(self.pageAction.selectedStatus);
                self.page.dropCondition.push(self.pageAction.selectedType);

                self.page.searchCondition.push(self.pageAction.searchProgramID);
                self.page.searchCondition.push(self.pageAction.searchVideoName);

                this.getData();
            
            },
            methods: {
                getData: function () { // 获取数据
                    var self=this;
                    var postData={}; 
                    var dropCon=self.page.dropCondition;
                    var searchCon=self.page.searchCondition;
                    postData["pageSize"]=self.page.pageSize;
                    postData["pageIndex"]=self.page.pageIndex;
                    postData["dropCondition"]= JSON.stringify(dropCon); 
                    postData["searchCondition"]= JSON.stringify(searchCon); 
                    $.post(url_getdata,postData,function(result){
                        console.info(result);
                        var code=result["code"];
                        if (code==0) {
                            self.data=JSON.parse(result["data"]);
                            self.totalCount=result["totalCount"];
                            self.pageCount=result["pageCount"];
                            self.page.pageIndex=parseInt(self.page.pageIndex);
                            self.pageCount=parseInt(self.pageCount);
                            if (self.page.pageIndex+4<self.pageCount) {
                                self.pageNumberList=[];
                                for(var i=self.page.pageIndex;i<=self.page.pageIndex+4;i++){
                                    self.pageNumberList.push(i);
                                }
                            }else{                                
                                self.pageNumberList=[];
                                if (self.pageCount>=5) {
                                     for(var i=self.pageCount-4;i<=self.pageCount;i++){                                        
                                        self.pageNumberList.push(i);
                                     }                                     
                                }else{
                                    for(var i=1;i<=self.pageCount;i++){
                                        self.pageNumberList.push(i);
                                    }                                
                                }                                
                            }
                        }                    
                    },"JSON")
                },
                toPage:function(action,num){ //页面跳转事件
                    console.info(action);
                    var self=this;
                    if (action=="toPage") {
                        if(self.pageAction.toPageIndex>self.pageCount){
                            self.pageAction.toPageIndex=self.pageCount;
                        }

                        self.page.pageIndex=self.pageAction.toPageIndex;
                    }
                    if (action=="FirstPage") {
                        self.page.pageIndex=1;
                    }
                    if (action=="Previous") {
                        if(self.page.pageIndex>1){
                            self.page.pageIndex--;
                        }
                    }
                    if (action=="Next") {
                        if(self.page.pageIndex<self.pageCount){
                            self.page.pageIndex++;
                        }
                    }
                    if (action=="LastPage") {
                        self.page.pageIndex=self.pageCount;
                    }
                    if (action=="number") {
                        self.page.pageIndex=parseInt(num);
                    }

                    self.getData();

                },
                toSearch:function(action){ //搜索事件
                    console.info(action);
                    var self=this;
                    if (action=="program") {
                        self.page.searchCondition[0]=self.pageAction.searchProgramID;
                    }
                    if (action=="video") {
                        self.page.searchCondition[1]=self.pageAction.searchVideoName;
                    }

                    self.getData();
                },
                btnUploadFile:function(){ // excel 文件上传
                    console.info("btnUploadFile");                
                },
                btnInsertXml:function(){  // 工单注入事件
                     console.info("btnInsertXml");        
                },
                selectChange:function(action){  // 下拉选择变化事件
                    console.info(action);
                    var self=this;
                    if (action=="status") {
                        self.page.dropCondition[0]=self.pageAction.selectedStatus;
                    }
                    if (action=="type") {
                        self.page.dropCondition[1]=self.pageAction.selectedType;
                    }
                    if (action=="pageSize") {
                        self.page.pageSize=self.pageAction.selectedPageSize;
                    }

                    self.getData();                
                },
                trCheckBox:function(id){   // 单条数据选择/取消
                    var self=this;
                    if(self.checkboxList.indexOf(id)>-1){
                        self.checkboxList.splice(self.checkboxList.indexOf(id),1)
                    }else{
                        self.checkboxList.push(id);                    
                    }
                },
                trCheckBoxAll:function(){ // 数据全部选择/取消
                    var self=this;
                    self.checkboxAll=!self.checkboxAll;
                    if(self.checkboxAll){
                        self.checkboxList=[];
                        $.each(self.data,function(index,item){                            
                            self.checkboxList.push(item.c_ProgramID);    
                        })                                        
                    }else{
                        self.checkboxList=[];  
                    }
                    
                },
                showPop:function(action,id){  // 展示弹窗
                    var self=this;
                    if (action=="show") {
                        $('#showModalLabel').modal();
                    }
                    if (action=="update") {
                        $('#updateModalLabel').modal();
                    }
                
                }
            }
        })
    </script>
</body>
</html>
