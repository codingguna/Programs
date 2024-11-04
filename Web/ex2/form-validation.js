function validateform(){
            const errorElements=document.querySelectorAll('.error');
            errorElements.forEach(element => element.remove());
            let isvalid=true;
            const username=document.getElementById('username').value;
            if(username === ''){
                showError('username','username is required');
            isvalid=false;
            }else if(username.length<3){
                showError('username','username must be at least 3 characters');
                isvalid=false;
            }
            const email=document.getElementById('email').value;
            if(email === ''){
                showError('email','email is required');
                isvalid=false;
            }else if(!validateEmail(email)){
                showError('email','please enter valid emailaddress');
                isvalid=false;
            }const pass=document.getElementById('password').value;
            if(pass === ''){
                showError('password','password is required');
            isvalid=false;
            }else if(pass.length<6){
                showError('password','password must be at least 6 characters');
                isvalid=false;
            }
            const age=document.getElementById('age').value;
            if(age === ''){
                showError('age','age is required');
            isvalid=false;
            }else if(age<18 || age>100){
                showError('age','age must between 18 and 100');
                isvalid=false;
            }
            
            if(isvalid==true){
                window.alert('form submited scussfully');
            };
            return isvalid;
        };
            


        function showError(fieldId,message){
            const field=document.getElementById(fieldId);
            const error=document.createElement('div');
            error.className='error';
            error.innerText=message;
            field.parentNode.insertBefore(error,field.nextSibling);
        };
        function validateEmail(email){
            const re=/^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
            return re.test(String(email).toLowerCase());
        };