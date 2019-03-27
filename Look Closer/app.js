
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
        }
    
        async function perform()
        {
            l = ["ready?",108, 97, 103, 123, 116, 104, 51, 95, 99, 108, 48, 115, 51, 114, 95, 121, 48, 117, 95, 108, 48, 48, 107, 95, 116, 104, 51, 95, 108, 51, 115, 115, 95, 121, 48, 117, 95, 115, 51, 51, 125,"hope you caught that"];
    
            var pophere = document.getElementById("pophere");
            for(var i = 0; i<l.length; i++)
            {
                pophere.innerText = l[i];
                if(i == 0) await sleep(1700);
                await sleep(300);
            }
    
        }
        window.onload = perform;