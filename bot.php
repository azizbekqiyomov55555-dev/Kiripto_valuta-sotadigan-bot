<?php
ob_start();

/*
Yomon kayfiyat bilan kod tarqatmoqchiman, buni oxiri voy bo'lmasa bo'lgani 😥
Ushbu kod har doimgiday @AlijonovUz ga tegishlik.
manbani o'zgartirganlaringni ko'rib qolsam xafa qilaman!
*/

define("AlijonovUz",'@AlijonovUz');
$admin = "8537782289"
$user = file_get_contents("admin/user.txt");
$bot = bot('getme',['8527362840:AAEHwbiUGYLPbnWBY-b8nfmhLYeajxPL744'])->result->username;


function name($ch){
$c = bot('getchat',['chat_id' => "@".$ch]);
return $c->result->title;
}

function getAdmin($chat){
$url = "https://api.telegram.org/bot".AlijonovUz."/getChatAdministrators?chat_id=@".$chat;
$result = file_get_contents($url);
$result = json_decode ($result);
return $result->ok;
}

function bot($method,$datas=[]){
	$url = "https://api.telegram.org/bot".AlijonovUz."/".$method;
	$ch = curl_init();
	curl_setopt($ch,CURLOPT_URL,$url);
	curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
	curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
	$res = curl_exec($ch);
	if(curl_error($ch)){
		var_dump(curl_error($ch));
	}else{
		return json_decode($res);
	}
}

$alijonov = json_decode(file_get_contents('php://input'));
$message = $alijonov->message;
$tx = $message->text;
$cid = $message->chat->id;
$mid = $message->message_id;
$text = $message->text;
$chat_id = $message->chat->id;
$message_id = $message->message_id;
$from_id = $message->from->id;
$name = $message->from->first_name;
$username = $message->from->username;
$bio = $message->from->about;

$data = $alijonov->callback_query->data;
$qid = $alijonov->callback_query->id;
$cid2 = $alijonov->callback_query->message->chat->id;
$mid2 = $alijonov->callback_query->message->message_id;
$callfrid = $alijonov->callback_query->from->id;
$callname = $alijonov->callback_query->from->first_name;
$calluser = $alijonov->callback_query->from->username;
$surname = $alijonov->callback_query->from->last_name;
$about = $alijonov->callback_query->from->about;

$step = file_get_contents("step/$cid.step");
$pul = file_get_contents("pul/$cid.txt");
$odam = file_get_contents("odam/$cid.txt");
$ban = file_get_contents("ban/$cid.txt");
$baza = file_get_contents("azo.dat");

$valyuta = file_get_contents("admin/valyuta.txt");
$taklif = file_get_contents("admin/taklif.txt");
$narx = file_get_contents("admin/narx.txt");
$narx2 = file_get_contents("admin/narx2.txt");
$saved = file_get_contents("step/alijonov.txt");
$aktiv = file_get_contents("nakrutka/$cid/aktiv.txt");
$qiwi = file_get_contents("admin/qiwi.txt");
$kanal = file_get_contents("admin/kanal.txt");
$tak = file_get_contents("admin/key.txt");
$manzil = file_get_contents("nakrutka/$cid/manzil.txt");
$miqdor = file_get_contents("nakrutka/$cid/miqdor.txt");
$mes = file_get_contents("nakrutka/user/$mid.txt");

if(file_get_contents("admin/taklif.txt")){
	}else{
		if(file_put_contents("admin/taklif.txt","1"));
}
if(file_get_contents("admin/valyuta.txt")){
	}else{
		if(file_put_contents("admin/valyuta.txt","₽"));
}
if(file_get_contents("admin/narx.txt")){
	}else{
		if(file_put_contents("admin/narx.txt","0.3"));
}
if(file_get_contents("admin/narx2.txt")){
	}else{
		if(file_put_contents("admin/narx2.txt","0.2"));
}
if(file_get_contents("admin/kanal.txt")){
	}else{
	   if(file_put_contents("admin/kanal.txt","Kiritilmagan"));
}
if(file_get_contents("admin/user.txt")){
	}else{
		if(file_put_contents("admin/user.txt","Kiritilmagan"));
}
if(file_get_contents("admin/qiwi.txt")){
	}else{
		if(file_put_contents("admin/qiwi.txt","Kiritilmagan"));
}
	
mkdir("ban");
mkdir("pul");
mkdir("odam");
mkdir("admin");
mkdir("step");
mkdir("nakrutka");
mkdir("nakrutka/user");
mkdir("nakrutka/$cid");

$panel = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"⚙ Asosiy sozlamalar"]],
[['text'=>"📊 Statistika"],['text'=>"✉ Xabar yuborish"]],
[['text'=>"🔎 Foydalanuvchini boshqarish"]],
[['text'=>"📂 Script"],['text'=>"◀️ Orqaga"]]
]
]);

$menu = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"💵 Pul yig'ish"]],
[['text'=>"👔 Kabinet"],['text'=>"🛍 Buyurtma"]],
[['text'=>"🔗 Takliflar"]],
]
]);

$menus = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"💵 Pul yig'ish"]],
[['text'=>"👔 Kabinet"],['text'=>"🛍 Buyurtma"]],
[['text'=>"🔗 Takliflar"],['text'=>"🗄 Boshqarish"]]
]
]);

$back = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"◀️ Orqaga"]],
]
]);

$boshqarish = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 Boshqarish"]],
]
]);

if($text){
if($ban == "ban"){
exit();
}else{
}
}

if($data){
$ban = file_get_contents("ban/$cid2.txt");
if($ban == "ban"){
exit();
}else{
}
}

if(isset($message)){
$pul = file_get_contents("pul/$cid.txt");
$mm=$pul+0;
file_put_contents("pul/$cid.txt","$mm");
$odam = file_get_contents("odam/$cid.txt");
$kkd=$odam+0;
file_put_contents("odam/$cid.txt","$kkd");
}

if(isset($message)){
   $baza=file_get_contents("azo.dat");
   if(mb_stripos($baza,$chat_id) !==false){
   }else{
   $txt="\n$chat_id";
   $file=fopen("azo.dat","a");
   fwrite($file,$txt);
   fclose($file);
   }
}

//<---- @AlijonovUz ----->//

if($text == "/start"){
	if($cid != $admin){
		bot('SendMessage',[
		'chat_id'=>$cid,
		'text'=>"🚀 @$bot <b>ga xush kelibsiz!</b>",
		'parse_mode'=>'html',
		'reply_markup'=>$menu,
		]);
exit();
	}else{
		bot('SendMessage',[
		'chat_id'=>$admin,
		'text'=>"🚀 @$bot <b>ga xush kelibsiz!</b>",
		'parse_mode'=>'html',
		'reply_markup'=>$menus,
		]);
exit();
	}
}

	if(mb_stripos($text,"/start")!==false){
$refid = explode(" ",$text);
$refid = $refid[1];
if(strlen($refid)>0 and $refid>0){
if($refid == $cid){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"🚀 @$bot <b>ga xush kelibsiz!</b>",
'parse_mode'=>'html',
'reply_markup'=>$menu,
]);
exit();
}else{
if(mb_stripos($baza,"$cid")!==false){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"🚀 @$bot <b>ga xush kelibsiz!</b>",
'parse_mode'=>'html',
'reply_markup'=>$menu
]);
exit();
}else{
$pul = file_get_contents("pul/$refid.txt");
$a = $pul + $taklif;
file_put_contents("pul/$refid.txt","$a");
$odam = file_get_contents("odam/$refid.txt");
$b = $odam + $taklif;
file_put_contents("odam/$refid.txt","$b");
bot('sendMessage',[
'chat_id'=>$cid,
    'text'=>"🚀 @$bot <b>ga xush kelibsiz!</b>",
    'parse_mode'=>'html',
'reply_markup'=>$menu,
]);
bot('SendMessage',[
'chat_id'=>$refid,
'text'=>"<b>➕ Sizda yangi taklif bor</b>

<i>Sizga $taklif $valyuta berildi</i>",
'parse_mode'=>'html',
]);
exit();
}
}
}
}

if($text == "◀️ Orqaga"){
	if($cid != $admin){
		bot('SendMessage',[
		'chat_id'=>$cid,
		'text'=>"<b>Bosh menyuga qaytdingiz.</b>",
		'parse_mode'=>'html',
		'reply_markup'=>$menu,
		]);
		unlink("step/$cid.step");
	exit();
	}else{
		bot('SendMessage',[
		'chat_id'=>$admin,
		'text'=>"<b>Bosh menyuga qaytdingiz.</b>",
		'parse_mode'=>'html',
		'reply_markup'=>$menus,
		]);
		unlink("step/$cid.step");
	exit();
	}
}

if($text == "💵 Pul yig'ish"){
$kan = str_replace("@","",$kanal);
	bot('SendMessage',[
	'chat_id'=>$cid,
	'text'=>"<b>Quyidagilardan birini tanlang: ⤵️</b>",
	'parse_mode'=>'html',
	'reply_markup'=>json_encode([
	'inline_keyboard'=>[
	[['text'=>"$tak",'url'=>"https://t.me/$kan"]],
[['text'=>"🔗 Takliflar",'callback_data'=>"takliflar"]]
]
])
]);
exit();
}

if($data == "takliflar"){
$odam = file_get_contents("odam/$cid2.txt");
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"<b>📱 Sizning taklif havolangiz:</b>

https://t.me/$bot?start=$cid2
<b>Taklif narxi: $taklif $valyuta

Taklfilaringiz soni: $odam ta</b>",
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
]);
}

if($text == "🔗 Takliflar"){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📱 Sizning taklif havolangiz:</b>

https://t.me/$bot?start=$cid
<b>Taklif narxi: $taklif $valyuta

Taklfilaringiz soni: $odam ta</b>",
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
]);
exit();
}

if($text == "👔 Kabinet"){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>🔑 Sizning ID raqamingiz:</b> <code>$cid</code>

💵 <b>Umumiy balansingiz: $pul $valyuta
👥 Takliflaringiz soni: $odam ta</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"💳 Pul kiritish",'callback_data'=>"oplata"]]
]
])
]);
exit();
}

if($data == "kabinet"){
$pul = file_get_contents("pul/$cid2.txt");
$odam = file_get_contents("odam/$cid2.txt");
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"<b>🔑 Sizning ID raqamingiz:</b> <code>$cid2</code>

💵 <b>Umumiy balansingiz: $pul $valyuta
👥 Takliflaringiz soni: $odam ta</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"💳 Pul kiritish",'callback_data'=>"oplata"]]
]
])
]);
}

if($data == "oplata"){
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<b>💳 Quyidagi to'lov tizimlaridan birni tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"QIWI",'callback_data'=>"qiwi"]],
   [['text'=>"◀️ Orqaga",'callback_data'=>"kabinet"]]
]
])
]);
}

//<---- @AlijonovUz ----->//

if($data == "qiwi"){
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<b>💳 To'lov tizimi:</b> QIWI

<b>Hamyon:</b> <code>$qiwi</code>
<b>Izoh:</b> <code>$cid2</code>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
   [['text'=>"◀️ Orqaga",'callback_data'=>"oplata"]]
]
])
]);
}

if($text == "🛍 Buyurtma"){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"🛍 <b>Buyurtma turini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"📢 Kanal",'callback_data'=>"kanal"]],
]
])
]);
exit();
}

if($data == "buyurtma"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"🛍 <b>Buyurtma turini tanlang:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"📢 Kanal",'callback_data'=>"kanal"]],
]
])
]);
}

if($data == "kanal"){
$pul = file_get_contents("pul/$cid2.txt");
$min = $pul / $narx;
$max = floor($min);
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"📢 <b>Ushbu bot kanalingizga obunachilar yig'ib olishingizga yordam beradi</b>

👤 1 ta obunachi - <b>$narx $valyuta</b>
💳 Balansingiz: <b>$pul $valyuta</b>
📊 Siz <b>$max ta obunachini</b> buyurtma qilishingiz mumkin

❗️ <b>Diqqat! Kanalingizni qo'shishdan olding @$bot ni kanalingizda admin qilishingiz kerak!</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"➕ Kanal qo'shish",'callback_data'=>"add"]],
[['text'=>"⏱ Aktiv buyurtmalar",'callback_data'=>"aktiv"]],
[['text'=>"◀️ Orqaga",'callback_data'=>"buyurtma"]]
]
])
]);
}

if($data == "aktiv"){
$aktiv = file_get_contents("nakrutka/$cid2/aktiv.txt");
$soni = substr_count($aktiv,"@");
	if($aktiv == null){
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>'html',
]);
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>'html',
]);
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"🤷‍♂️ <b>Sizga tegishli aktiv buyurtmalar topilmadi!</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"kanal"]]
]
])
]);
}else{
$mid3 = file_get_contents("nakrutka/$cid2/mid.txt");
$b = file_get_contents("nakrutka/user/$mid3.txt");
$mes = substr_count($b,"\n");
	bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>'html',
]);
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"⏱ <b>Yuklanmoqda...</b>",
'parse_mode'=>'html',
]);
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<b>Aktiv buyurtmalaringiz (maks. x1)</b> ⤵️
➖➖➖➖➖➖➖➖
<i>No. Buyurtma | Miqdor | Bajarildi</i>
➖➖➖➖➖➖➖➖

$aktiv | $mes

<b>Barcha natijalar:</b> $soni ta",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"kanal"]]
]
])
]);
}
}

if($data == "add"){
if($kanal != "Kiritilmagan"){
$aktiv = file_get_contents("nakrutka/$cid2/aktiv.txt");
if($aktiv == null){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('sendMessage',[
'chat_id'=>$cid2,
'text'=>"<b>Buyurtma miqdorini yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$back,
]);
file_put_contents("step/$cid2.step",'miqdor');
}else{
bot('answerCallbackQuery',[
'callback_query_id'=>$qid,
'text'=>"Sizda aktiv buyurtma mavjud!",
'show_alert'=>true,
]);
}
}else{
bot('answerCallbackQuery',[
'callback_query_id'=>$qid,
'text'=>"Vazifalar kanali ulanmagan!",
'show_alert'=>true,
]);
}
}

//<---- @AlijonovUz ----->//

if($step == "miqdor"){
$min = "2";
$max = "1000";
if(is_numeric($text)=="true"){
if($text >= $min and $text <= $max){
$alijonov = $text * $narx;
if($pul >= $alijonov){
file_put_contents("nakrutka/$cid/miqdor.txt",$text);
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Buyurtma miqdori: $text ta</b>

<i>Kanalingiz manzilini yuboring:</i>

Namuna: $kanal",
'parse_mode'=>'html',
]);
file_put_contents("step/$cid.step",'manzil');
exit();
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Ushbu miqdordagi buyurtma uchun hisobingizda yetarli mablag' mavjud emas!</b>

Buyurtma miqdorini qayta kiriting:",
'parse_mode'=>'html',
]);
exit();
}
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Minimal buyurtma miqdori - 10 ta, 
Maksimal buyurtma miqdori - 1000 ta</b>

Buyurtma miqdorini qayta kiriting:",
'parse_mode'=>'html',
]);
exit();
}
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Buyurtma miqdorini raqamlardan foydalanib kiriting:</b>",
'parse_mode'=>'html',
]);
exit();
}
}

if($step == "manzil"){
if(stripos($text,"@")!==false){
$get = bot('getChat',[
'chat_id'=>$text
]);
$types = $get->result->type;
$ch_name = $get->result->title;
$ch_user = $get->result->username;
if(getAdmin($ch_user)== true){
file_put_contents("nakrutka/$cid/manzil.txt",$text);
$aktiv = file_get_contents("nakrutka/$cid/aktiv.txt");
file_put_contents("nakrutka/$cid/aktiv.txt","@$ch_user | $miqdor");
$m = $miqdor * $narx;
file_put_contents("pul/$cid.txt",$m);
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Tayyor!</b>

$text i uchun buyurtma qabul qilindi.",
'parse_mode'=>'html',
]);
unlink("step/$cid.step");
$msg = bot('SendMessage',[
'chat_id'=>$kanal,
'text'=>"✅ Quyidagi kanalga obuna bo'ling:
➡️ @$ch_user
💵 <b>Va tekshirish tugmasini bosing!
🤖 Botga o'tish:</b> @$bot",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"📳 Kanalga o'tish",'url'=>"https://t.me/$ch_user"]],
[['text'=>"💵 Tekshirish",'callback_data'=>"tekshir=$miqdor=$cid=$ch_user"]],
]
])
])->result->message_id;
file_put_contents("nakrutka/$cid/mid.txt",$msg);
exit();
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>@$bot ushbu kanalda admin emas!</b>

<i>Botni kanalga admin qilib tayinlab, qayta urinib ko'ring:</i>",
'parse_mode'=>'html',
]);
exit();
}
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>❗️ Manzil $kanal ko'rinishda bo'lishi kerak.</b>

<i>Qayta urinib ko'ring.</i>",
'parse_mode'=>'html',
]);
exit();
}
}


if(stripos($data,"tekshir=")!==false && stripos($baza,"$callfrid")!==false){
$ex = explode("=",$data);
$miqdor = $ex[1];
$id = $ex[2];
$manzil = $ex[3];
$ue = file_get_contents("nakrutka/user/$mid2.txt");
if(stripos($ue,"$callfrid") !== false){
bot('answercallbackquery', [
'callback_query_id'=>$qid,
'text'=>"Siz ushbu vazifani allaqachon bajargansiz.",
'show_alert'=> true,
]);
}else{
$okch = json_decode(file_get_contents("https://api.telegram.org/bot".AlijonovUz."/getChatMember?chat_id=@".$manzil."&user_id=".$callfrid))->result->status;
if($okch=='member' || $okch=='creator' || $okch=='administrator'){
$user = substr_count(file_get_contents("nakrutka/user/$mid2.txt"),"\n");
$narx2 = file_get_contents("admin/narx2.txt");
if($user>=$narx2){
$narx2 = file_get_contents("admin/narx2.txt");
}else{
$narx2 = file_get_contents("admin/narx2.txt");
}
file_put_contents("nakrutka/user/$mid2.txt","\n".$callfrid,FILE_APPEND);
$pul = file_get_contents("pul/$callfrid.txt");
$puls = $pul + $narx2;
file_put_contents("pul/$callfrid.txt","$puls");
bot('answercallbackquery',[
'callback_query_id'=>$qid,
'text'=>"💰 Kanalga obuna bo'ldingiz va hisobingizga $narx2 $valyuta qo'shildi",
'show_alert'=> true,
]);     
}else{
bot('answercallbackquery', [
'callback_query_id'=>$qid,
'text'=>"⛔ Kanalga obuna bo'lmadingiz!",
'show_alert'=> true,
]);
}
}
$okey = substr_count(file_get_contents("nakrutka/user/$mid2.txt"),"\n");
if($okey>=$miqdor){
$post = file_get_contents("nakrutka/$id/mid.txt");
bot('deleteMessage',[
'chat_id'=>$kanal,
'message_id'=>$post,
]);
bot('sendMessage',[
"chat_id"=>$id,
"text"=>"✅ <b>Sizning @$manzil buyurtmangiz muvaffaqiyatli bajarildi!</b>",
"parse_mode"=>'html',
]);
exit();
unlink("nakrutka/user/$mid2.txt");
unlink("nakrutka/$id/aktiv.txt");
}
if(getAdmin($manzil) != true){
$post = file_get_contents("nakrutka/$id/mid.txt");
bot('deleteMessage',[
'chat_id'=>$kanal,
'message_id'=>$post,
]);
bot('sendMessage',[
"chat_id"=>$id,
'text'=>"🛍 <b>Buyurtmangiz bekor qilindi!

Sababi:</b> Bot kanaldan adminlikdan olindi.",
"parse_mode"=>'html',
]);
unlink("nakrutka/user/$mid2.txt");
unlink("nakrutka/$id/aktiv.txt");
exit();
}   
}

//<---- @AlijonovUz ----->//

//<- Admin Panel ->\\

if($text == "🗄 Boshqarish" and $cid == $admin){
	bot('SendMessage',[
	'chat_id'=>$admin,
	'text'=>"<b>Boshqaruv panelidasiz:</b>",
	'parse_mode'=>'html',
	'reply_markup'=>$panel,
	]);
	unlink("step/alijonov.txt");
	unlink("step/$cid.step");
	exit();
}

if($data == "boshqaruv"){
	bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
	'text'=>"<b>Boshqaruv panelidasiz:</b>",
	'parse_mode'=>'html',
	'reply_markup'=>$panel,
	]);
exit();
}

if($text == "📂 Script"){
if($cid == $admin){
bot('sendDocument',[
'chat_id'=>$admin,
'document'=>new CURLFile(__FILE__),
'caption'=>"<b>@$bot kodi</b>",
'parse_mode'=>'html',
]);
exit();
}
}

if($data == "foydalanuvchi"){
if(file_exists("ban/$saved.txt")){
$pul = file_get_contents("pul/$saved.txt");
$odam = file_get_contents("odam/$saved.txt");
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"<b>Foydalanuvchi topildi!

ID:</b> <a href='tg://user?id=$saved'>$saved</a>

<b>Balansi: $pul $valyuta
Takliflari: $odam ta</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🔕 Bandan olish",'callback_data'=>"unban"]],
[['text'=>"➕ Pul qo'shish",'callback_data'=>"plus"],['text'=>"➖ Pul ayirish",'callback_data'=>"minus"]]
]
])
]);
}else{
$pul = file_get_contents("pul/$saved.txt");
$odam = file_get_contents("odam/$saved.txt");
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"<b>Foydalanuvchi topildi!

ID:</b> <a href='tg://user?id=$saved'>$saved</a>

<b>Balansi: $pul $valyuta
Takliflari: $odam ta</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🔔 Banlash",'callback_data'=>"ban"]],
[['text'=>"➕ Pul qo'shish",'callback_data'=>"plus"],['text'=>"➖ Pul ayirish",'callback_data'=>"minus"]]
]
])
]);
}
}

if($text == "🔎 Foydalanuvchini boshqarish"){
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Kerakli foydalanuvchining ID raqamini yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish
]);
file_put_contents("step/$cid.step",'iD');
exit();
}

if($step == "iD"){
if(file_exists("pul/$text.txt")){
if(file_exists("ban/$text.txt")){
file_put_contents("step/alijonov.txt",$text);
$pul = file_get_contents("pul/$text.txt");
$odam = file_get_contents("odam/$text.txt");
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Foydalanuvchi topildi!

ID:</b> <a href='tg://user?id=$text'>$text</a>

<b>Balansi: $pul $valyuta
Takliflari: $odam ta</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🔕 Bandan olish",'callback_data'=>"unban"]],
[['text'=>"➕ Pul qo'shish",'callback_data'=>"plus"],['text'=>"➖ Pul ayirish",'callback_data'=>"minus"]]
]
])
]);
unlink("step/$cid.step");
exit();
}else{
file_put_contents("step/alijonov.txt",$text);
$pul = file_get_contents("pul/$text.txt");
$odam = file_get_contents("odam/$text.txt");
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Foydalanuvchi topildi!

ID:</b> <a href='tg://user?id=$text'>$text</a>

<b>Balansi: $pul $valyuta
Takliflari: $odam ta</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"🔔 Banlash",'callback_data'=>"ban"]],
[['text'=>"➕ Pul qo'shish",'callback_data'=>"plus"],['text'=>"➖ Pul ayirish",'callback_data'=>"minus"]]
]
])
]);
unlink("step/$cid.step");
exit();
}
}else{
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Ushbu foydalanuvchi botdan foydalanmaydi!</b>

<i>Boshqa ID raqamni kiriting:</i>",
'parse_mode'=>'html',
]);
exit();
}
}


//qo'shish
if($data == "plus"){
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<a href='tg://user?id=$saved'>$saved</a> <b>ning hisobiga qancha pul qo'shmoqchisiz?</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"foydalanuvchi"]],
]
])
]);
file_put_contents("step/$cid2.step",'plus');
}

if($step == "plus"){
if(is_numeric($text)=="true"){
bot('sendMessage',[
'chat_id'=>$saved,
'text'=>"<b>Adminlar tomonidan hisobingiz $text $valyuta to'ldirildi</b>",
'parse_mode'=>"html",
'reply_markup'=>$menu,
]);
bot('sendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Foydalanuvchi hisobiga $text $valyuta qo'shildi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
$pul = file_get_contents("pul/$saved.txt");
$miqdor = $pul + $text;
file_put_contents("pul/$saved.txt",$miqdor);
unlink("step/alijonov.txt");
unlink("step/$cid.step");
exit();
}else{
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
'protect_content'=>true,
]);
exit();
}
}

//ayirish
if($data=="minus"){
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<a href='tg://user?id=$saved'>$saved</a> <b>ning hisobiga qancha pul ayirmoqchisiz?</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"foydalanuvchi"]]
]
])
]);
file_put_contents("step/$cid2.step",'minus');
}

if($step == "minus"){
if(is_numeric($text)=="true"){
bot('sendMessage',[
'chat_id'=>$saved,
'text'=>"<b>Adminlar tomonidan hisobingizdan $text $valyuta olib tashlandi</b>",
'parse_mode'=>"html",
'reply_markup'=>$menu,
]);
bot('sendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Foydalanuvchi hisobidan $text $valyuta olib tashlandi!</b>",
'parse_mode'=>"html",
'reply_markup'=>$panel,
]);
$pul = file_get_contents("pul/$saved.txt");
$miqdor = $pul - $text;
file_put_contents("pul/$saved.txt",$miqdor);
unlink("step/alijonov.txt");
unlink("step/$cid.step");
exit();
}else{
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
]);
exit();
}
}

if($data=="ban"){
if($admin != $saved){
file_put_contents("ban/$saved.txt",'ban');
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<a href='tg://user?id=$saved'>$saved</a> <b>banlandi</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"foydalanuvchi"]]
]
])
]);
exit();
}else{
bot('answerCallbackQuery',[
'callback_query_id'=>$qid,
'text'=>"Asosiy adminlarni blocklash mumkin emas!",
'show_alert'=>true,
]);
}
}

if($data=="unban"){
unlink("ban/$saved.txt");
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<a href='tg://user?id=$saved'>$saved</a> <b>banlandan olindi</b>",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"foydalanuvchi"]]
]
])
]);
exit();
}

//<---- @AlijonovUz ----->//

if($text == "✉ Xabar yuborish"){
if($cid == $admin){
	bot('SendMessage',[
	'chat_id'=>$cid,
	'text'=>"<b>Yuboriladigan xabar turini tanlang;</b>",
	'parse_mode'=>'html',
	'reply_markup'=>json_encode([
	'inline_keyboard'=>[
	[['text'=>"Userga",'callback_data'=>"user"]],
	[['text'=>"Oddiy",'callback_data'=>"send"]],
	]
	])
	]);
exit();
}
}

if($data == "user"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"<b>Foydalanuvchi iD raqamini kiriting:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'user');
}

if($step == "user"){
if($cid == $admin){
if(is_numeric($text)=="true"){
file_put_contents("step/alijonov.txt",$text);
	bot('SendMessage',[
	'chat_id'=>$cid,
	'text'=>"<b>Xabaringizni kiriting:</b>",
	'parse_mode'=>'html',
	]);
file_put_contents("step/$cid.step",'xabar');
exit();
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
]);
exit();
}
}
}

if($step == "xabar"){
if($cid == $admin){
	bot('SendMessage',[
	'chat_id'=>$saved,
	'text'=>"$text",
        'parse_mode'=>'html',
'disable_web_page_preview'=>true,
'protect_content'=>true,
	]);
	bot('SendMessage',[
	'chat_id'=>$admin,
	'text'=>"<b>Xabaringiz yuborildi ✅</b>",
       'parse_mode'=>'html',
        'reply_markup'=>$panel,
	]);
	unlink("step/$cid.step");
	unlink("step/alijonov.txt");
exit();
}
}

if($data == "send"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"*Xabaringizni kiriting:*",
'parse_mode'=>"markdown",
'reply_markup'=>$boshqarish
]);
 file_put_contents("step/$cid2.step","users");
exit();
}
if($step=="users"){
if($cid == $admin){
$lich = file_get_contents("azo.dat");
$lichka = explode("\n",$lich);
foreach($lichka as $lichkalar){
$okuser=bot("sendmessage",[
'chat_id'=>$lichkalar,
'text'=>$text,
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
'protect_content'=>true,
]);
exit();
}
}
}
if($okuser){
bot("sendmessage",[
'chat_id'=>$admin,
'text'=>"<b>Hammaga yuborildi ✅</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel
]);
unlink("step/$cid.step");
exit();
}

if($text == "📊 Statistika"){
	if($cid == $admin){
$baza = file_get_contents("azo.dat");
$obsh = substr_count($baza,"\n");
$start_time = round(microtime(true) * 1000);
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"",
'parse_mode'=>'html',
]);
$end_time = round(microtime(true) * 1000);
$ping = $end_time - $start_time;
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"💡 <b>PING:</b> <code>$ping</code>

👥 <b>Foydalanuvchilar:</b> $obsh ta",
'parse_mode'=>'html',
]);
exit();
}
}


if($text == "⚙ Asosiy sozlamalar"){
		if($cid == $admin){
	bot('SendMessage',[
	'chat_id'=>$cid,
	'text'=>"<b>⚙️ Asosiy sozlamalar bo'limiga xush kelibsiz!</b>

<i>Nimani o'zgartiramiz?</i>",
	'parse_mode'=>'html',
	'reply_markup'=>json_encode([
	'inline_keyboard'=>[
	[['text'=>"📋 Hozirgi holat",'callback_data'=>"holat"]],
	[['text'=>"🔗 Taklif narxi",'callback_data'=>"narx"],['text'=>"💶 Valyuta",'callback_data'=>"valyuta"]],
	[['text'=>"👤 1 ta obunachi narxi",'callback_data'=>"ObuNarx"]],
	[['text'=>"💴 1 ta obunachi uchun to'lov",'callback_data'=>"ObuTolov"]],
	[['text'=>"🐤 QIWI hamyon",'callback_data'=>"hamyon"],['text'=>"📢 Vazifalar kanali",'callback_data'=>"vazchannel"]],
	[['text'=>"☎️ Admin useri",'callback_data'=>"admin"],['text'=>"◀️ Orqaga",'callback_data'=>"boshqaruv"]],
]
])
]);
exit();
}
}

if($data == "asosiy"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
	'text'=>"<b>⚙️ Asosiy sozlamalar bo'limiga xush kelibsiz!</b>

<i>Nimani o'zgartiramiz?</i>",
	'parse_mode'=>'html',
	'reply_markup'=>json_encode([
	'inline_keyboard'=>[
	[['text'=>"📋 Hozirgi holat",'callback_data'=>"holat"]],
	[['text'=>"🔗 Taklif narxi",'callback_data'=>"narx"],['text'=>"💶 Valyuta",'callback_data'=>"valyuta"]],
	[['text'=>"👤 1 ta obunachi narxi",'callback_data'=>"ObuNarx"]],
	[['text'=>"💴 1 ta obunachi uchun to'lov",'callback_data'=>"ObuTolov"]],
	[['text'=>"🐤 QIWI hamyon",'callback_data'=>"hamyon"],['text'=>"📢 Vazifalar kanali",'callback_data'=>"vazchannel"]],
	[['text'=>"☎️ Admin useri",'callback_data'=>"admin"],['text'=>"◀️ Orqaga",'callback_data'=>"boshqaruv"]],
]
])
]);
exit();
}

if($data == "holat"){
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<b>Kuting...</b>",
'parse_mode'=>'html',
]);
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2 + 1,
'text'=>"<b>Kuting...</b>",
'parse_mode'=>'html',
]);
bot('editMessageText',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
'text'=>"<b>Hozirgi sozlamalar:</b>

<i>1. Taklif narxi - $taklif $valyuta
2. Valyuta - $valyuta
3. 1 ta obunachi narxi - $narx $valyuta
4. 1 ta obuna uchun to'lov - $narx2 $valyuta
5. QIWI hamyon - $qiwi
6. Vazifalar kanali - $kanal
7. Admin useri - $user</i>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"◀️ Orqaga",'callback_data'=>"asosiy"]],
]
])
]);
exit();
}


if($data == "valyuta"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"📝 <b>Yangi qiymatni yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'valyuta');
exit();
}

if($step == "valyuta" and $cid == $admin){
if(isset($text)){
file_put_contents("admin/valyuta.txt",$text);
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.step");
exit();
}
}

if($data == "narx"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"📝 <b>Yangi qiymatni yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'taklif');
exit();
}

if($step == "taklif" and $cid == $admin){
if(is_numeric($text)==true){
file_put_contents("admin/taklif.txt",$text);
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.step");
exit();
}else{
	bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
]);
exit();
}
}

//<---- @AlijonovUz ----->//

if($data == "ObuNarx"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"📝 <b>Yangi qiymatni yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'narx');
exit();
}

if($step == "narx" and $cid == $admin){
if(is_numeric($text)==true){
file_put_contents("admin/narx.txt",$text);
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.step");
exit();
}else{
	bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
]);
exit();
}
}

if($data == "ObuTolov"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"📝 <b>Yangi qiymatni yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'narx2');
exit();
}

if($step == "narx2" and $cid == $admin){
if(is_numeric($text)==true){
file_put_contents("admin/narx2.txt",$text);
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.step");
exit();
}else{
	bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
]);
exit();
}
}

if($data == "hamyon"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"📝 <b>Yangi qiymatni yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'qiwi');
exit();
}

if($step == "qiwi" and $cid == $admin){
if(is_numeric($text)==true){
file_put_contents("admin/qiwi.txt",$text);
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.step");
exit();
}else{
	bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
]);
exit();
}
}

if($data == "vazchannel"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"📝 <b>Yangi qiymatni yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'vazchannel');
exit();
}

if($step == "vazchannel" and $cid == $admin){
if(stripos($text,"@")!==false){
$get = bot('getChat',[
'chat_id'=>$text
]);
$types = $get->result->type;
$ch_name = $get->result->title;
$ch_user = $get->result->username;
if(getAdmin($ch_user)== true){
file_put_contents("admin/kanal.txt","@$ch_user");
file_put_contents("admin/key.txt","📢 Kanallarga obuna bo'lish");
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.step");
exit();
}else{
	bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>Bot ushbu kanalda admin emas yoki noto'g'ri kanal manzili yuborildi!</b>",
'parse_mode'=>'html',
]);
exit();
}
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚠️ Kanal manzili kiritishda xatolik.</b>

<i>Qayta urinib ko'ring.</i>",
'parse_mode'=>'html',
]);
exit();
}
}


if($data == "admin"){
bot('deleteMessage',[
'chat_id'=>$cid2,
'message_id'=>$mid2,
]);
bot('SendMessage',[
'chat_id'=>$cid2,
'text'=>"📝 <b>Yangi qiymatni yuboring:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("step/$cid2.step",'admin');
exit();
}

if($step == "admin" and $cid == $admin){
if(stripos($text,"@")!==false){
file_put_contents("admin/user.txt",$text);
bot('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Muvaffaqiyatli o'zgartirildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("step/$cid.step");
exit();
}else{
bot('SendMessage',[
'chat_id'=>$cid,
'text'=>"<b>⚠️ Admin userini kiritishda xatolik.</b>

<i>Qayta urinib ko'ring.</i>",
'parse_mode'=>'html',
]);
exit();
}
}

if($text != "/start" or $text != "💵 Pul yig'ish" or $text != "🛍 Buyurtma" or $text != "👔 Kabinet" or $text != "🔗 Takliflar" or $text != "🗄 Boshqarish" or $text != "⚙ Asosiy sozlamalar" or $text != "📊 Statistika" or $text != "✉ Xabar yuborish" or $text != "🔎 Foydalanuvchini boshqarish" or $text != "💵 To'lov holati" or $text != "◀️ Orqaga"){
	/*if($step != "miqdor" or $step != "manzil" or $step != "iD" or $step != "plus" or $step != "minus" or $step != "user" or $step != "xabar" or $step != "users" or $step != "valyuta" or $step != "taklif" or $step != "narx" or $step != "narx2" or $step != "qiwi" or $step != "vazchannel" or $step != "admin"){*/
		if($cid != $admin){
		bot('SendMessage',[
		'chat_id'=>$cid,
		'text'=>"🚀 @$bot <b>ga xush kelibsiz!</b>",
		'parse_mode'=>'html',
		'reply_markup'=>$menu,
		]);
	}else{
		bot('SendMessage',[
		'chat_id'=>$admin,
		'text'=>"🚀 @$bot <b>ga xush kelibsiz!</b>",
		'parse_mode'=>'html',
		'reply_markup'=>$menus,
		]);
	}
}

//<---- @AlijonovUz ----->//

?>
