

import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.*;

@WebServlet("/HitCount")
public class HitCount extends HttpServlet {
	private static final long serialVersionUID = 1L;
    public HitCount() {
        super();
    }

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session =request.getSession();
		Integer count=(Integer)session.getAttribute("hitcount");
		if(count==null) {
			count=1;
		}else {
			count++;
		}
		session.setAttribute("hitcount", count);
		
		response.setContentType("text/html");
		PrintWriter out=response.getWriter();
		out.println(+count);		
	}
}
