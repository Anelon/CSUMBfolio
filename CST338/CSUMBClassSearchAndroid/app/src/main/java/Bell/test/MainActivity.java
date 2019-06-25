package Bell.test;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Map;
import java.util.TreeMap;

public class MainActivity extends AppCompatActivity {

   EditText searchNumberInput;
   Button searchButton;
   TextView searchResult;

   TreeMap<String, String> classNumToDesc = new TreeMap<>();

   protected void showAllClasses() {
      String resultText = "";
      //for all of the entries in classNumToDesc add that class to resultText
      for(Map.Entry<String, String> clas : classNumToDesc.entrySet()) {
         String className = getString(R.string.classTag) + clas.getKey();
         String classDesc = clas.getValue();
          resultText += className + "\n" + classDesc + "\n\n";
      }

      searchResult.setText(resultText);
      searchResult.setVisibility(View.VISIBLE);
   }

   @Override
   protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
      Log.d("LifeCycleEvent", "onCreate: in");

      //set up id's to associated variables
      searchNumberInput = findViewById(R.id.searchNumberInput);
      searchButton = findViewById(R.id.searchButton);
      searchResult = findViewById(R.id.searchResult);

      searchResult.setVisibility(View.GONE);

      //fill Class Dictionary
      classNumToDesc.put("300", "Helps  identify and articulate personal, professional, and social"+
         " goals. Provides an integrated overview of the computer science and communication design"+
         " majors and their requirements. Students develop a plan for their learning goals."+
         " Students learn writing, presentation, research and critical-thinking skills within the"+
         " diversified fields of information technology and communication design. Students learn"+
         " how to analyze, predict, and articulate trends in the academic, public service.");
      classNumToDesc.put("205", "Introduces design, creation, and manipulation of interactive"+
         " applications and electronic media for communication purpose. Focuses on creating media,"+
         " understanding media concepts, and manipulating the created media using basic"+
         " programming concepts of control flow, functions, expressions and data types in the"+
         " Python language. Students acquire a basic understanding for digital media formats, how"+
         " to design, create such media using basic programming skills.");
      classNumToDesc.put("338", "Provides students with the fundamental concepts to develop"+
         " large-scale software, focusing on the object-oriented programming techniques. Coverage"+
         " includes the introduction to Java programming language, object-oriented programming,"+
         " software life cycle and development processes, requirements analysis, and graphical"+
         " user interface development.");
      classNumToDesc.put("361", "Tech Tutors satisfies the ITCD Major Learning Outcome, Service "+
         "Learning in the Major; and the Culture and Equity ULR. During 15 weeks of the semester, "+
         "students are required to spend a minimum of 30 hours applying skills and knowledge " +
         "acquired in their studies at either a K-12 school or a non-profit agency registered in " +
         "the CSUMB Service Learning Institute’s database. Students will study the " +
         "“digital divide”, observe and reflect on social and cultural identities, and social " +
         "injustice while performing their service. The steps of the project include analysis of " +
         "their partner’s training and technological needs; submitting a proposal to solve those " +
         "needs; and implementation. Community Partner’s constituents may include students, " +
         "teachers, parents, and staff. ");
      classNumToDesc.put("363", "This course provides balanced coverage of database use and " +
         "design, focusing on relational databases. Students will learn to design relational " +
         "schemas, write SQL queries, access a DB programmatically,and perform database " +
         "administration. Students will gain a working knowledge of the algorithms and data " +
         "structures used in query evaluation and transaction processing. Students will also " +
         "learn to apply newer database technologies such as XML, NoSQL, and Hadoop.");
      classNumToDesc.put("311", "Survey of Telecomm and Data Comm Technology Fundamentals, Local " +
         "Area Network, Wide Area Network, Internet and internetworking protocols including " +
         "TCP/IP, network security and performance, emerging industry trends such as voice over " +
         "the network and high speed networking. Designed as a foundation for students who wish " +
         "to pursue more advanced network studies including certificate programs. Includes " +
         "hands-on networking labs that incorporate Cisco CCNA lab components.");
      classNumToDesc.put("336", "Provides students with dynamic web application development " +
         "skills, focusing on the integration of server-side programming, database connectivity, " +
         "and client-side scripting. Coverage includes the Internet architecture, responsive " +
         "design, RESTful web services, and Web APIs.");
      classNumToDesc.put("325", "This course teaches the students the fundamentals of game " +
         "programming and skills needed for game development, including GPU programming, matrix " +
         "and quaternion algebra for physics calculation, animation, lighting and basics of " +
         "implementing 3D models into a framework.");
      classNumToDesc.put("370", "Students learn important data structures in computer science " +
         "and acquire fundamental algorithm design techniques to get the efficient solutions to " +
         "several computing problems from various disciplines. Topics include the analysis of " +
         "algorithm efficiency, hash, heap, graph, tree, sorting and searching, brute force, " +
         "divide-and-conquer, decrease-and-conquer, transform-and-conquer, dynamic programming, " +
         "and greedy programming.");
      classNumToDesc.put("438", "Prepares students for large-scale software development using " +
         "software engineering principles and techniques. Coverage includes software process, " +
         "requirements analysis and specification, software design, implementation, testing, and " +
         "project management. Students are expected to work in teams to carry out a " +
         "realistic software project.");
      classNumToDesc.put("499", "Students will work on a project in large groups (up to 5 " +
         "students in each group), developing requirements specification, a solution plan " +
         "followed by design and implementation of the solution. The problem statement for the " +
         "projects will be selected by the faculty. Faculty will also play the role of a " +
         "project manager directing the schedule and deliverables for these projects.");

      //Show all classes as default
      showAllClasses();

      searchButton.setOnClickListener(new View.OnClickListener() {
         @Override
         public void onClick(View view) {
            String classID = searchNumberInput.getText().toString().trim();

            //if search string is empty reset to show all classes
            if(classID.length() == 0) {
               //show all classes
               showAllClasses();
               return;
            }
            //initialize result strings in case there isn't any result
            String resultName = "Class Does Not Exist";
            String resultDesc = "please try again.";

            //if classID is valid show that class and Description
            if(classNumToDesc.containsKey(classID)) {
               resultName = getString(R.string.classTag) + classID;
               resultDesc = classNumToDesc.get(classID).toString();
            }
            String resultText = resultName + "\n" + resultDesc;

            searchResult.setText(resultText);
         }
      });
   }

}
