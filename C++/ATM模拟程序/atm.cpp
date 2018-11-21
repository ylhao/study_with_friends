#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>


using namespace std;


class BankCard {
public:
	BankCard() {}
	BankCard(string id, string password, int balance);
	string getId();
	string getPassword(); // 获取密码
	void setPassword(string password); // 设置密码
	int getBalance(); // 获取余额
	void setBalance(int balance); // 设置余额
private:
	string id;
	string password;
	int balance;
};

BankCard::BankCard(string id, string password, int balance) {
	this->id = id;
	this->password = password;
	this->balance = balance;
}

string BankCard::getId() {
	return this->id;
}

string BankCard::getPassword() {
	return this->password;
}

void BankCard::setPassword(string password) {
	this->password = password;
}

int BankCard::getBalance() {
	return this->balance;
}

void BankCard::setBalance(int balance) {
	this->balance = balance;
}


class ATM {
public:
	ATM(BankCard& bc);
	bool check(); // 验证身份
	void showMenu();
	void query();
	void saveMoney();
	void getMoney();
	bool transfer();
	void resetPassword();
	void start();
	void exit();
	string inputPassword();
private:
	BankCard bc;
};

ATM::ATM(BankCard& bc) {
	this->bc = bc;
}

bool ATM::check() {
	int count = 0;
	string password = "";
	bool flag = false;
	cout << "输入密码（您一共有 3 次机会）：";
	while (count < 3) {
		password = inputPassword();
		if (this->bc.getPassword().compare(password) == 0) {
			flag = true;
			break;
		}
		else {
			cout << "密码错误，请重新输入密码：";
		}
		count++;
	}
	return flag;
}

void ATM::query() {
	cout << "卡号：" << this->bc.getId() << endl;
	// cout << "密码：" << this->bc.getPassword() << endl; // 如果为了验证密码可以取消注释验证一下
	cout << "余额：" << this->bc.getBalance() << endl;
}

void ATM::saveMoney() {
	int value = 0;
	cout << "请输入存款金额：";
	cin >> value;
	while (true) {
		if (value % 100 != 0 || value == 0) {
			cout << "存款金额必须是 100 的整数倍（且不能为0），请重新输入取款金额：";
			cin >> value;
		}
		else if (value > 5000) { // 单次存款金额不能超过 5000
			cout << "单次存款金额不能超过 5000，请重新输入取款金额：";
			cin >> value;
		}
		else {
			break;
		}
	}
	this->bc.setBalance(this -> bc.getBalance() + value); // 更新余额
	cout << "卡内余额：" << this->bc.getBalance() << endl;
}

void ATM::getMoney() {
	int value = 0;
	cout << "请输入取款金额：";
	cin >> value;
	while (true) {
		if (value % 100 != 0 || value == 0) {
			cout << "取款金额必须是 100 的整数倍（且不能为0），请重新输入取款金额：";
			cin >> value;
		}
		else if (value > this->bc.getBalance()) {
			cout << "余额不足，请重新输入取款金额：";
			cin >> value;
		}
		else {
			break;
		}
	}
	this->bc.setBalance(this -> bc.getBalance() - value); // 更新余额
	cout << "卡内余额：" << this->bc.getBalance() << endl;
}

bool ATM::transfer() {
	BankCard bc1 = BankCard("1234567891234567891", "123456", 10000);
	BankCard bc2 = BankCard("1234567891234567892", "123456", 10000);
	BankCard bc3 = BankCard("1234567891234567893", "123456", 10000);
	BankCard bc4 = BankCard("1234567891234567894", "123456", 10000);
	BankCard bc5 = BankCard("1234567891234567895", "123456", 10000);
	BankCard bcs[5] = { bc1, bc2, bc3, bc4, bc5 };
	// 输入卡号
	cout << "请输入对方卡号：";
	string id;
	cin >> id;
	// 判断输入的卡号是否合法
	bool flagId = false;
	int i = 0;
	for (i = 0; i < 5; i++) {
		if (bcs[i].getId().compare(id) == 0) { // 判断输入的卡号是否是以上定义的 5 个卡号中的一个
			flagId = true;
			break;
		}
	}
	if (flagId == false) {
		cout << "卡号不在操作允许范围内，不予转账！" << endl;
		return false;  // 转账失败
	}
	cout << "请输入转账金额：";
	int value = 0; // 转出金额
	cin >> value;
	if (value > this->bc.getBalance()) { // 判断余额是否充足 
		cout << "余额不足" << endl;
		return false; // 转账失败
	}
	if (value <= 0) { // 转账金额不能为 0 或负数
		cout << "非法操作" << endl;
		return false; // 转账失败
	}
	this->bc.setBalance(this->bc.getBalance() - value);
	cout << "卡内余额：" << this->bc.getBalance() << endl;
	cout << "转入卡号：" << bcs[i].getId() << endl;
	cout << "转入前金额:" << bcs[i].getBalance() << endl;
	bcs[i].setBalance(bcs[i].getBalance() + value);
	cout << "转入后金额:" << bcs[i].getBalance() << endl;
	return true; // 转账成功
}

void ATM::resetPassword() {
	cout << "输入旧密码：";
	string password;
	password = inputPassword();
	// cin >> password;
	if (this->bc.getPassword().compare(password) == 0) {
		string password1;
		string password2;
		cout << "输入新密码：";
		// cin >> password1;
		password1 = inputPassword();
		cout << "再次确认新密码:";
		// cin >> password2;
		password2 = inputPassword();
		if (password1.compare(password2) == 0) {
			this->bc.setPassword(password1);
		}
		else {
			cout << "两次输入的密码不一致" << endl;
		}
	}
	else {
		cout << "旧密码输入有误" << endl;
	}
}

void ATM::exit() {
	cout << "您已退出系统" << endl;
}

void ATM::showMenu() {
	cout << "  余额查询-----------------------1" << endl;
	cout << "  存    款-----------------------2" << endl;
	cout << "  取    款-----------------------3" << endl;
	cout << "  转    账-----------------------4" << endl;
	cout << "  修改密码-----------------------5" << endl;
	cout << "  退    出-----------------------0" << endl;
}

void ATM::start() {
	int choice;
	while (true) {
		showMenu();
		cout << endl;
		cout << "请输入操作项：";
		cin >> choice;
		cout << endl;
		if (choice == 1) {
			query(); // 查询余额
		}
		else if (choice == 2) {
			saveMoney(); //存款
		}
		else if (choice == 3) {
			getMoney(); //取款
		}
		else if (choice == 4) {
			transfer(); // 转账
		}
		else if (choice == 5) {
			resetPassword(); // 重置密码
		}
		else if (choice == 0) {
			exit(); // 退出
			break;
		}
		else {
			continue;
		}
		cout << endl;
	}
}

string ATM::inputPassword() {
	char c;
	int count = 0;
	int size = 20;
	string str;
	char *password = new char[size];
	while ((c = _getch()) != '\r') {

		if (c == 8) { // 退格
			if (count == 0) {
				continue;
			}
			putchar('\b'); // 回退一格
			putchar(' '); // 输出一个空格将原来的 * 隐藏
			putchar('\b'); // 再回退一格等待输入
			count--;
		}
		if (count == size - 1) { // 最大长度为 size - 1
			continue;
		}
		if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {  // 密码只可包含数字和字母
			putchar('*');  // 每接收到一个字符打印一个 *
			password[count] = c;
			count++;
		}
	}
	password[count] = '\0';
	str = password;
	delete[] password; // 释放空间
	cout << endl;
	return str;
}

int main() {
	cout << "输入卡号：";
	string id;
	cin >> id;
	if (id.compare("1234567891234567890") != 0) {
		cout << "卡号错误" << endl;
		return 0;
	}
	BankCard bc0 = BankCard("1234567891234567890", "123456", 10000);
	ATM atm = ATM(bc0);
	bool flag = atm.check();
	if (flag) { // 校验身份成功
		atm.start();
	}
	else {  // 校验身份失败
		cout << "对不起，已吞卡，请联系相关部门进行处理！" << endl;
		return 0;
	}
}
