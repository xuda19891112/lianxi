#include <iostream>
#include <string>
using namespace std;
#define MAX 1000
// ��װ������ʾ�˵�
// main �������øú���

//�����ϵ�˽ṹ��
struct Person 
{
	// ����
	string m_Name;
	// �Ա� 1 �� 2  Ů
	int m_Sex;
	int m_Age;
	string m_Phone;
	string m_Addr;
};



//���ͨѶ¼�ṹ��
struct Addessbooks
{
	// ͨѶ¼�������ϵ������

	struct Person personArray[MAX];

	// ��ϵ�˸���
	int m_Size;
	

};

// 1�������ϵ��
void addPerson(Addessbooks* abs)
{
	//ͨѶ¼�Ƿ�����
	if (abs->m_Size == MAX)
	{
		cout << "ͨѶ¼�������޷����" << endl;
		return;
	}
	else
	{
		// ��Ӿ�����ϵ��

		string name;
		cout << "����������" << endl;
		cin >> name;
		abs->personArray[abs->m_Size].m_Name = name;
		
		cout << "�������Ա� " << endl;
		cout << "1-----�� " << endl;
		cout << "2-----Ů " << endl;
		int sex = 0;
		
		while (true)
		{
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[abs->m_Size].m_Sex = sex;
				break;
			}
			cout << "����������������" << endl;

		}

		cout << "����������" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[abs->m_Size].m_Age = age;

		cout << "��������ϵ�绰" << endl;
		string phone;
		cin >> phone;
		abs->personArray[abs->m_Size].m_Phone = phone;

		cout << "�������ͥסַ" << endl;
		string address;
		cin >> address;
		abs->personArray[abs->m_Size].m_Addr= address;

		abs->m_Size++;

		cout << "��ӳɹ�" << endl;

		system("pause");
		system("cls");



	}

}

// �˵�����

void showMenu()
{
	cout << "*************" << endl;
	cout << "1�������ϵ��" << endl;
	cout << "2����ʾ��ϵ��" << endl;
	cout << "3��ɾ����ϵ��" << endl;
	cout << "4��������ϵ��" << endl;
	cout << "5���޸���ϵ��" << endl;
	cout << "6�������ϵ��" << endl;
	cout << "0���˳�ͨѶ¼" << endl;
	cout << "*************" << endl;
} 




int main()
{
	// ����ͨѶ¼�ṹ�����
	Addessbooks abs;
	// ��ʼ����Ա����
	abs.m_Size = 0;
	

	//�û�ѡ�����
	int select = 0;

	while (true)
	{
		showMenu();

		cin >> select;
		switch (select)
		{
		case 1: // ���
			addPerson(&abs);
			break;
		case 2: //��ʾ
			break;
		case 3:  // ɾ��
			break;
		case 4:  //  ����
			break;
		case 5: //  �޸�
			break;
		case 6: // ���
			break;
		case 0:  //  ���
			cout << "��ӭ�´�ʹ��" << endl;
			system("pause");
			return 0;
		default:
			break;


		}
	
	
	}
	
	system("pause");
	return 0;
}