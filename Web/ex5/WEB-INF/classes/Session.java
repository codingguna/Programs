import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.*;

@WebServlet("/Session")
public class Session extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException {
        response.setContentType("text/html");
        String name = request.getParameter("name");

        HttpSession session = request.getSession();
        session.setAttribute("name", name);

        PrintWriter out = response.getWriter();
        out.println("<html><head><title>session tracking</title></head>");
        out.println("<body><h2>Hello, " + name + "!</h2>");
        out.println("<p>your session id :" + session.getId() + "</p>");
        out.println("</body></html>");
    }
}