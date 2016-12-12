package domain;

public class Cliente {
boolean invitado;
String nombre;
String passwd;
public Cliente(String nombre, String passwd) {
	super();
	this.nombre = nombre;
	this.passwd = passwd;
	this.invitado = false;
}
public Cliente() {
	super();
	this.invitado=true;
	this.nombre= "invitado";
	this.passwd= " ";
}
public boolean isInvitado() {
	return invitado;
}
public void setInvitado(boolean invitado) {
	this.invitado = invitado;
}
public String getNombre() {
	return nombre;
}
public void setNombre(String nombre) {
	this.nombre = nombre;
}
public String getPasswd() {
	return passwd;
}
public void setPasswd(String passwd) {
	this.passwd = passwd;
}


}
