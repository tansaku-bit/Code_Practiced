public class Reminder {

	private String name;

	private int priority;

	public void show() {
		System.out.printf(name+"("+priority+")"+"\n");
	}

	public Reminder() {
		this.name = "no name";
		priority = 0;

	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getPriority() {
		return priority;
	}

	public void setPriority(int priority) {
		this.priority = priority;
	}

}
