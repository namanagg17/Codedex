
    class Employee {
        int salary;
        String name;

        public int getsalary() {
            return salary;
        }

        public void setsalary(int s) {
            salary = s;
        }

        public String getname() {
            return name;
        }

        public void setname(String n) {
            name = n;
        }
    }
    public class PS_7 {
    public void main(String[] args) {
        Employee naman = new Employee();
        naman.setname("naman");
        naman.salary = 50000;
        System.out.println(naman.getsalary());
        System.out.println(naman.getname());
    }
}