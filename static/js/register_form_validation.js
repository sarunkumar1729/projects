// $(document).ready(function() {
//       $("#registerForm").submit(function(event) {
//           // Prevent default form submission
//           event.preventDefault();
  
//           // Clear previous error messages
//           $(".error").remove();
  
//           // Get form values
//           var email = $("#email").val();
//           var password = $("#password").val();
//           var confirmPassword = $("#confirmPassword").val();
//           var isValid = true;
  
//           // Email validation
//           if (!validateEmail(email)) {
//               $("#email").after('<span class="error">Enter a valid email</span>');
//               isValid = false;
//           }
  
//           // Password validation
//           if (!validatePassword(password)) {
//               $("#password").after('<span class="error">Password must contain at least one lowercase letter, one uppercase letter, and one number</span>');
//               isValid = false;
//           }
  
//           // Confirm password validation
//           if (password !== confirmPassword) {
//               $("#confirmPassword").after('<span class="error">Passwords do not match</span>');
//               isValid = false;
//           }
  
//           if (isValid) {
//             //   alert("Form is valid! Submitting...");
//             this.submit();
//               // Here you can write code to submit the form
//           }
//       });
  
//       function validateEmail(email) {
//           var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//           return re.test(email);
//       }
  
//       function validatePassword(password) {
//           var re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$/;
//           return re.test(password);
//       }
//   });
  

