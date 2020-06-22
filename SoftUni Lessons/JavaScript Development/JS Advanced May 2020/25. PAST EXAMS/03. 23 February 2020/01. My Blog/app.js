function solve(){

    document.querySelectorAll('button')[0].addEventListener('click',add);

    function add(e){
        e.preventDefault();
        let title=document.getElementById('title').value;
        let category=document.getElementById('category').value;
        let content=document.getElementById('content').value;
        let creator=document.getElementById('creator').value;

        if(!title||!category||!content||!creator) { return; }

        let article = document.createElement('article');
        article.innerHTML=`<h1>${title}</h1><p>Category:<strong> ${category}</strong></p><p>Creator:<strong> ${creator}</strong></p><p>${content}</p><div class="buttons"><button class="btn delete">Delete</button><button class="btn archive">Archive</button></div>`;
        let appendElement=document.querySelector('main > section');
        appendElement.appendChild(article);

        let[deleteBtn,archiveBtn]=article.querySelectorAll('button');

        deleteBtn.addEventListener('click',()=>{
            appendElement.removeChild(article)
        });

        archiveBtn.addEventListener('click',()=>{
            appendElement.removeChild(article);
            let li= document.createElement('li');
            li.innerHTML=title;

            let ul=document.querySelector('.archive-section > ul');
            ul.appendChild(li);
            const items= [...ul.querySelectorAll('li')];
            ul.innerHTML='';

            items.sort((a,b)=>a.textContent.localeCompare(b.textContent))
                .forEach(e=>ul.appendChild(e))
        });
        title.value="";
    }
}
