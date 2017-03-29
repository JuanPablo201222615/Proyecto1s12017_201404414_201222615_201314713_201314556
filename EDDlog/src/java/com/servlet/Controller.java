/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.servlet;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.RequestBody;
import java.io.IOException;
import java.io.PrintWriter;
import java.security.SecureRandom;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import static com.servlet.Client.getString;

/**
 *
 * @author dell
 */
public class Controller extends HttpServlet {
    Client cliente = new Client();
static final String AB = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
static SecureRandom rnd = new SecureRandom();
  String message1;
  String idac;
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
         HttpSession session = request.getSession();
        response.setContentType("text/html;charset=UTF-8");
        if(request.getParameter("btnlogin") != null){
        try (PrintWriter out = response.getWriter()) {
          String _username=request.getParameter("txtusername");
          String _password=request.getParameter("txtpassword");
          String _empresa=request.getParameter("txtempresa");
          String _departamento=request.getParameter("txtdepartamento");
          message1 = _username + "," + _password + "," + _empresa + "," + _departamento + ";";    
       //   System.out.println(message1);
        
          try{
                RequestBody formBody = new FormEncodingBuilder()
                .add("username", _username)
                .add("password", _password)
                .add("empresa", _empresa)
                .add("departamento", _departamento)
                .build();
        String r = getString("userdata", formBody); 
        System.out.println("Este " + r);
              if (_username!=null){
                  if(Integer.valueOf(r) == 1){
               
                     
                      session.setAttribute("user", _username);
                     session.setAttribute("pass", _password);
                     session.setAttribute("empr", _empresa);
                     session.setAttribute("depa", _departamento);
                      response.sendRedirect("welcome.jsp");
                         }
                  else{
                  out.println("Login Failed, try again");
                  }
                  
              }
          }
          catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
        }}
         if(request.getParameter("btnregister") != null){
              response.sendRedirect("registro.jsp");
         }
           if(request.getParameter("btnreturn") != null){
              response.sendRedirect("index.jsp");
         }
              if(request.getParameter("btnreturn2") != null){
              response.sendRedirect("welcome.jsp");
         }
            if(request.getParameter("btnagregar") != null){
                 idac= randomString(15);
              session.setAttribute("nombreactivo", idac);  
                response.sendRedirect("activo.jsp");
         }
if(request.getParameter("btneliminar") != null){
                  session.setAttribute("idacti", "000000000");
                   session.setAttribute("nomeli", "Nombre");
                  session.setAttribute("desceli", "");
                     try (PrintWriter out = response.getWriter()) {
                         String empresa=(String) session.getAttribute("empr");
         String user=(String) session.getAttribute("user");
           String departamento=(String) session.getAttribute("depa");
                try{
                    
                RequestBody formBody = new FormEncodingBuilder()
                 .add("empresas",empresa)
                 .add("users",user)
                .add("departamentos",departamento)
                .build();
        String r = getString("populate", formBody); 
        System.out.println("cadena: " + r);
       String [] stringarray = r.split("\\s*,\\s*");
       int a=0;
              while (a < stringarray.length) {
            System.out.println(stringarray[a]);
            a=a+1;
              }
              
        session.setAttribute("stringarray",stringarray);
         response.sendRedirect("activoe.jsp");
          }
          catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
                    }
         }
if(request.getParameter("refresel") != null){
                    try (PrintWriter out = response.getWriter()) {
                String dropnow =request.getParameter("dropdown1");
                  System.out.println(dropnow);
                try{
                RequestBody formBody = new FormEncodingBuilder()
                .add("drop1", dropnow)
                .build();
        String r = getString("refresh1", formBody); 
        String [] rarray = r.split("\\s*,\\s*");
        System.out.println("Este " + r);
          
         session.setAttribute("desceli", rarray[1]);
          session.setAttribute("nomeli", rarray[0]);
         response.sendRedirect("activoe.jsp");
          }
          catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
                    }
                
         }
if(request.getParameter("btnmodificar") != null){
                  session.setAttribute("idactim", "000000000");
                   session.setAttribute("nommod", "Nombre");
                  session.setAttribute("descmod", "");
                  
                  try (PrintWriter out = response.getWriter()) {
                         String empresa=(String) session.getAttribute("empr");
         String user=(String) session.getAttribute("user");
           String departamento=(String) session.getAttribute("depa");
                try{
                RequestBody formBody = new FormEncodingBuilder()
                 .add("empresas",empresa)
                 .add("users",user)
                .add("departamentos",departamento)
                .build();
        String r = getString("populate", formBody); 
        System.out.println("cadena: " + r);
       String [] stringarray = r.split("\\s*,\\s*");
       int a=0;
              while (a < stringarray.length) {
            System.out.println(stringarray[a]);
            a=a+1;
              }
        session.setAttribute("stringarray",stringarray);
         response.sendRedirect("activom.jsp");
          }
          catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
                    }
                
             
         }
 if(request.getParameter("refresmod") != null){
                    try (PrintWriter out = response.getWriter()) {
                String dropnow =request.getParameter("dropdown2");
                  System.out.println(dropnow);
                try{
                RequestBody formBody = new FormEncodingBuilder()
                .add("drop2", dropnow)
                .build();
        String r = getString("refresh2", formBody); 
        String [] rarray = r.split("\\s*,\\s*");;
        System.out.println("Este " + r);
          
         session.setAttribute("descmod", rarray[1]);
          session.setAttribute("nommod", rarray[0]);
         response.sendRedirect("activom.jsp");
          }
          catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
                    }
                
         }

                if(request.getParameter("btnlogout") != null){
                   
              response.sendRedirect("index.jsp");
         }
if(request.getParameter("btnagregaract") != null){
             try (PrintWriter out = response.getWriter()) {
       
        String nameact=request.getParameter("txtnombreact");
        String descripcion=request.getParameter("description");
        String empresa=(String) session.getAttribute("empr");
         String user=(String) session.getAttribute("user");
           String departamento=(String) session.getAttribute("depa");
          String message2 = idac + "," + nameact + "," + descripcion;
                  try{
              RequestBody formBody2 = new FormEncodingBuilder()
                .add("idactivo",idac)
                .add("nombreactivo",nameact)
                .add("descripcion",descripcion)
                .add("empresact",empresa)
                 .add("useract",user)
                .add("departamentoact",departamento)
                .build();
        String r2= getString("newactivo", formBody2); 
        System.out.println("Este " + r2);
          response.sendRedirect("welcome.jsp");
                     }
           catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
         }
             
         } 
                
    if(request.getParameter("btneliminaract") != null){
           try (PrintWriter out = response.getWriter()) {
                String idaac =request.getParameter("dropdown1");
                  String empresa=(String) session.getAttribute("empr");
         String user=(String) session.getAttribute("user");
           String departamento=(String) session.getAttribute("depa");
                  System.out.println(idaac);
                try{
                RequestBody formBody = new FormEncodingBuilder()
                        
                 .add("empresas",empresa)
                 .add("users",user)
                .add("departamentos",departamento)
                .add("idactivoel", idaac)
                .build();
        String r = getString("eliminaractivo", formBody); 
        System.out.println("Este " + r);
          
         session.setAttribute("desceli", "");
          session.setAttribute("nomeli", "Nombre");
         response.sendRedirect("activoe.jsp");
          }
          catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
                    }
                
                  }
                  
   if(request.getParameter("btnmodificaract") != null){
        try (PrintWriter out = response.getWriter()) {
                String idaac =request.getParameter("dropdown2");
                  String empresa=(String) session.getAttribute("empr");
         String user=(String) session.getAttribute("user");
           String departamento=(String) session.getAttribute("depa");
                  System.out.println(idaac);
                try{
                    
                RequestBody formBody = new FormEncodingBuilder()
                        
              .add("empresas",empresa)
                 .add("users",user)
                .add("departamentos",departamento)
                .add("idactivom", idaac)
                .build();
        String r = getString("modificaractivo", formBody); 
        System.out.println("Este " + r);
          
         session.setAttribute("desceli", r);
         response.sendRedirect("activoe.jsp");
          }
          catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
                    }
                
   }
   
   if(request.getParameter("btncreateuser") != null){
        try (PrintWriter out = response.getWriter()) {
          String _username=request.getParameter("txtusername2");
          String _password=request.getParameter("txtpassword2");
          String _name=request.getParameter("txtname2");
          String _empresa=request.getParameter("txtempresa2");
          String _departamento=request.getParameter("txtdepartamento2");
          
          try{
           RequestBody formBody = new FormEncodingBuilder()
                .add("username", _username)
                .add("password", _password)
                .add("name", _name)
                .add("empresa", _empresa)
                .add("departamento", _departamento)
                .build();
        String r2 = getString("newuserdata", formBody); 
        System.out.println("Este " + r2);
        response.sendRedirect("index.jsp");
          }
           catch(Exception e){
              out.print("Error: " + e.getMessage());
          }
         }}
          
         
    }
String randomString( int len ){
   StringBuilder sb = new StringBuilder( len );
   for( int i = 0; i < len; i++ ) 
      sb.append( AB.charAt( rnd.nextInt(AB.length()) ) );
   return sb.toString();
}


    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }

    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
