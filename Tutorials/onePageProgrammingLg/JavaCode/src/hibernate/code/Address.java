package hibernate.code;

import javax.persistence.Embeddable;

@Embeddable
public class Address {
	public static Address createAddress(String city, int pin) {
		return new Address(city, pin);
	}

	private String city;
	private int pin;

	private Address(String city, int pin) {
		this.city = city;
		this.pin = pin;
	}

	public String getCity() {
		return city;
	}

	public int getPin() {
		return pin;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public void setPin(int pin) {
		this.pin = pin;
	}

	@Override
	public String toString() {
		return "Address [city=" + city + ", pin=" + pin + "]";
	}

}
