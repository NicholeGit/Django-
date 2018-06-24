### waterfall 瀑布流示例

创建数据表

python manage.py makemigrations waterfall

python manage.py migrate waterfall

重点是img.html文件

建立四个`<div>`，循环把`<img>`标签放入其中。

```js
<script>
	$(function () {
	var obj = new ScrollImg()
	obj.initImg();
	obj.scrollEvent();
	});
	function ScrollImg(){
		this.nid = 0;
		this.lastPostion = 0;
		this.initImg =  function () {
			var that = this;
			$.ajax({
				url:'./get_imgs.html',
				type:'GET',
				dataType:'JSON',
				data:{nid:that.nid},
				success:function (arg) {
					var img_list = arg.data;
					$.each(img_list,function (index, v) {
						var eqv = (that.lastPostion + index) % 4;
						var tag = document.createElement('img');
						tag.src = '/' + v.src;
						$('#container').children().eq(eqv).append(tag);
						if (index+1==img_list.length){
							//that.nid = v.id;    //因为图片不多所以先屏蔽，这样可以反复加载
							that.lastPostion = eqv + 1;
						}
					})
				}
			})
		}
		//当滚轮到达最底部时，执行initImg（）
		this.scrollEvent = function() {
			var that = this;
			$(window).scroll(function() {
				var docHeight = $(document).height();  // 文档高度
				var winHeight = $(window).height();    // window高度
				var scrollTop = $(window).scrollTop(); // 滚动条滑动的高度
				if( (winHeight+scrollTop+1) >= docHeight){
					that.initImg()
				}
			})
		}
	}
</script>
```

