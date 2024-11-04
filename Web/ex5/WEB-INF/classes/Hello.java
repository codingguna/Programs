import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.*;

@WebServlet("/Hello")
public class Hello extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public Hello() {
        super();
    }
    @Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    	response.setContentType("text/html");
    	String name = request.getParameter("name");
    	String greeting="hello, "+name+"!";
    	PrintWriter out=response.getWriter();
    	out.println("<!doctype html><html><head><title>Greeting</title></head>");
    	out.println("<body><h1>"+greeting+"</h1></body></html>");
	}
}
