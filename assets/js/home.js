/* Renders the latest posts from /assets/data/tweets.json (refreshed by the
   "Update X posts" GitHub Action) into the sidebar card. Falls back to the
   static post baked into the HTML if the file can't be loaded. */
(function(){
  var embed=document.getElementById('x-embed');
  var fb=document.querySelector('.x-fallback');
  if(!embed) return;
  function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function linkify(s){
    s=esc(s);
    s=s.replace(/https?:\/\/[^\s<]+/g,function(u){return '<a href="'+u+'" target="_blank" rel="noopener">'+u.replace(/^https?:\/\//,'')+'</a>';});
    s=s.replace(/(^|[^\w@\/])@(\w{1,15})/g,'$1<a href="https://x.com/$2" target="_blank" rel="noopener">@$2</a>');
    s=s.replace(/(^|\s)#(\w+)/g,'$1<a href="https://x.com/hashtag/$2" target="_blank" rel="noopener">#$2</a>');
    return s;
  }
  function fmtDate(d){var dt=new Date(d);if(isNaN(dt.getTime()))return esc(d);return dt.toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric'});}
  function card(t){
    var url=t.url||'https://x.com/rebelsnlu_jaist';
    var media=t.photo?'<div class="x-tweet-media"><img loading="lazy" src="'+esc(t.photo)+'" alt=""></div>':'';
    var likes=(t.likes!=null&&t.likes!=='')?'<span aria-label="likes">♥ '+esc(t.likes)+'</span>':'';
    return '<article class="x-tweet">'
      +'<div class="x-tweet-top">'
        +'<span class="x-tweet-av" aria-hidden="true">R</span>'
        +'<div class="x-tweet-id"><span class="x-tweet-name">RebelsNLU@JAIST</span>'
        +'<span class="x-tweet-meta">@rebelsnlu_jaist · '+fmtDate(t.date)+'</span></div>'
      +'</div>'
      +'<p class="x-tweet-text">'+linkify(t.text||'')+'</p>'
      +media
      +'<div class="x-tweet-foot">'+likes+'<a href="'+esc(url)+'" target="_blank" rel="noopener">Read on X →</a></div>'
    +'</article>';
  }
  fetch('/assets/data/tweets.json',{cache:'no-cache'})
    .then(function(r){if(!r.ok)throw new Error('http '+r.status);return r.json();})
    .then(function(d){
      var list=(d&&d.tweets)||[];
      if(!list.length)throw new Error('empty');
      embed.innerHTML=list.slice(0,3).map(card).join('');
    })
    .catch(function(){ embed.style.display='none'; if(fb)fb.hidden=false; });
})();
