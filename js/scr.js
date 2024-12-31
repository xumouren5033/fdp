// 获取输入框元素和文件列表元素
const searchInput = document.getElementById('searchInput');
const fileList = document.getElementById('fileList');

// 为输入框添加输入事件监听器
searchInput.addEventListener('input', function () {
    const keyword = searchInput.value.toLowerCase(); // 获取输入的关键字并转为小写
    const listItems = fileList.querySelectorAll('li'); // 获取所有列表项

    // 遍历列表项，根据关键字进行显示或隐藏操作
    listItems.forEach(item => {
        const fileName = item.textContent.toLowerCase(); // 获取文件名并转为小写
        if (fileName.includes(keyword)) {
            item.style.display = 'block'; // 如果包含关键字则显示该项
        } else {
            item.style.display = 'none'; // 否则隐藏该项
        }
    });
});