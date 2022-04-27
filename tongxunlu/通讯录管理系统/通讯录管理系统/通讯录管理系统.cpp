#include <iostream>
#include <string>
using namespace std;
#define MAX 1000
// 封装函数显示菜单
// main 函数调用该函数

//设计联系人结构体
struct Person 
{
	// 姓名
	string m_Name;
	// 性别 1 男 2  女
	int m_Sex;
	int m_Age;
	string m_Phone;
	string m_Addr;
};



//设计通讯录结构体
struct Addessbooks
{
	// 通讯录保存的联系人数组

	struct Person personArray[MAX];

	// 联系人个数
	int m_Size;
	

};

// 1、添加联系人
void addPerson(Addessbooks* abs)
{
	//通讯录是否已满
	if (abs->m_Size == MAX)
	{
		cout << "通讯录已满，无法添加" << endl;
		return;
	}
	else
	{
		// 添加具体联系人

		string name;
		cout << "请输入姓名" << endl;
		cin >> name;
		abs->personArray[abs->m_Size].m_Name = name;
		
		cout << "请输入性别： " << endl;
		cout << "1-----男 " << endl;
		cout << "2-----女 " << endl;
		int sex = 0;
		
		while (true)
		{
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[abs->m_Size].m_Sex = sex;
				break;
			}
			cout << "输入有误，重新输入" << endl;

		}

		cout << "请输入年龄" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[abs->m_Size].m_Age = age;

		cout << "请输入联系电话" << endl;
		string phone;
		cin >> phone;
		abs->personArray[abs->m_Size].m_Phone = phone;

		cout << "请输入家庭住址" << endl;
		string address;
		cin >> address;
		abs->personArray[abs->m_Size].m_Addr= address;

		abs->m_Size++;

		cout << "添加成功" << endl;

		system("pause");
		system("cls");



	}

}

// 菜单界面

void showMenu()
{
	cout << "*************" << endl;
	cout << "1、添加联系人" << endl;
	cout << "2、显示联系人" << endl;
	cout << "3、删除联系人" << endl;
	cout << "4、查找联系人" << endl;
	cout << "5、修改联系人" << endl;
	cout << "6、清空联系人" << endl;
	cout << "0、退出通讯录" << endl;
	cout << "*************" << endl;
} 




int main()
{
	// 创建通讯录结构体变量
	Addessbooks abs;
	// 初始化人员个数
	abs.m_Size = 0;
	

	//用户选择变量
	int select = 0;

	while (true)
	{
		showMenu();

		cin >> select;
		switch (select)
		{
		case 1: // 添加
			addPerson(&abs);
			break;
		case 2: //显示
			break;
		case 3:  // 删除
			break;
		case 4:  //  查找
			break;
		case 5: //  修改
			break;
		case 6: // 情况
			break;
		case 0:  //  清空
			cout << "欢迎下次使用" << endl;
			system("pause");
			return 0;
		default:
			break;


		}
	
	
	}
	
	system("pause");
	return 0;
}