<?php

ob_start();
date_default_timezone_set("Asia/Tashkent");

define("scsmm","8527362840:AAEHwbiUGYLPbnWBY-b8nfmhLYeajxPL744");//bot tokeni kiritiladi//
$botname = scsmm('getme',['bot'])->result->username;
$admin = "8537782289";  //admin ID raqami kiritiladi//
$arays = array($arays,$admin);
//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
function addstat($id){
    $check = file_get_contents("scsmm.bot");
    $rd = explode("\n",$check);
    if(!in_array($id,$rd)){
        file_put_contents("scsmm.bot","\n".$id,FILE_APPEND);

    }
}

function banstat($id){
    $check = file_get_contents("scsmm.ban");
    $rd = explode("\n",$check);
    if(!in_array($id,$rd)){
        file_put_contents("scsmm.ban","\n".$id,FILE_APPEND);
    }
}

function step($id,$value){
file_put_contents("scsmm/$id.step","$value");
}

function stepbot($id,$value){
file_put_contents("scsmmbot/$id.step","$value");
}

function typing($chatid){ 
return scsmm("sendChatAction",[
"chat_id"=>$chatid,
"action"=>"typing",
]);
}

function joinchat($id){
global $message_id,$referalsum,$firstname;
$array = array("inline_keyboard");
$get = file_get_contents("scsmm/kanal.txt");
if($get == null){
return true;
}else{
$ex = explode("\n",$get);
for($i=0;$i<=count($ex) -1;$i++){
$first_line = $ex[$i];
$first_ex = explode("@",$first_line);
$url = $first_ex[1];
$name=scsmm('getChat',['chat_id'=>"@".$url,])->result->title;
     $ret = scsmm("getChatMember",[
         "chat_id"=>"@$url",
         "user_id"=>$id,
         ]);
$stat = $ret->result->status;
         if((($stat=="creator" or $stat=="administrator" or $stat=="member"))){
      $array['inline_keyboard']["$i"][0]['text'] = " ". $name;
$array['inline_keyboard']["$i"][0]['url'] = "https://t.me/$url";
         }else{
$array['inline_keyboard']["$i"][0]['text'] = " ". $name;
$array['inline_keyboard']["$i"][0]['url'] = "https://t.me/$url";
$uns = true;
}
}
$array['inline_keyboard']["$i"][0]['text'] = "✅ Tekshirish";
$array['inline_keyboard']["$i"][0]['callback_data'] = "result";
if($uns == true){
   scsmm("sendMessage",[
         "chat_id"=>$id,
         "text"=>"<b>Assalomu Alaykum, botdan to`liq foydalanish uchun quydagi kanallarga obuna bo`ling, Obunangizni tasdiqlash uchun ( ✅ Tekshirish )! tugmasini bosing.</b>",
         "parse_mode"=>"html",
         "reply_to_message_id"=>$mid,
"disable_web_page_preview"=>true,
"reply_markup"=>json_encode($array),
]);  
sleep(2);
     if(file_exists("scsmm/".$id.".referalid")){
           $file =  file_get_contents("scsmm/".$id.".referalid");
           $get =  file_get_contents("scsmm/".$id.".channel");
           if($get=="true"){
            file_put_contents("scsmm/".$id.".channel","failed");
            $minimal = $referalsum / 2;
            $user = file_get_contents("scsmm/".$file.".pul");
            $user = $user - $minimal;
            file_put_contents("scsmm/".$file.".pul","$user");
             scsmm("sendMessage",[
             "chat_id"=>$file,
             "text"=>"<b>Sizning do'stingiz</b>, <a href='tg://user?id=".$id."’>".$firstname."</a> <b>bizning kanallarimizdan chiqib ketgani uchun sizga ".$minimal."-$valbot jarima berildi.</b>",
             "parse_mode"=>"html",
             "reply_markup"=>$menu,
             ]);
           }
         }  
         return false;
}else{
return true;
}
}
}

function phonenumber($id){
     $phonenumber = file_get_contents("scsmm/$id.contact");
      if($phonenumber==true){
      return true;
         }else{
     stepbot($id,"request_contact");
     scsmm("sendMessage",[
    "chat_id"=>$id,
"photo"=>"",
    "text"=>"<b>Hurmatli foydalanuvchi!</b>\n<b>Pul ishlash ishonchli bo'lishi uchun, pastdagi «📲 Telefon raqamni yuborish» tugmasini bosing:</b>",
    "parse_mode"=>"html",
    "reply_markup"=>json_encode([
      "resize_keyboard"=>true,
      "one_time_keyboard"=>true,
      "keyboard"=>[
        [["text"=>"📲 Telefon raqamni yuborish","request_contact"=>true],],
]
]),
]);  
return false;
}
}

//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo

function scsmm($method,$datas=[]){
    $url = "https://api.telegram.org/bot".scsmm."/".$method;
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

$update = json_decode(file_get_contents('php://input’));
$bot_info = scsmm('getMe');
$bot_id = $bot_info->result->id;
$message = $update->message;
$callbackdata = $update->callback_query->data;
$chatid = $message->chat->id;
$chat_id = $update->callback_query->message->chat->id;
$type = $message->chat->type;
$messageid = $message->message_id;
$id = $update->callback_query->id;
$fromid = $message->from->id;
$from_id = $update->callback_query->from->id;
$firstname = $message->from->first_name;
$first_name = $update->callback_query->from->first_name;
$lastname = $message->from->last_name;
$message_id = $update->callback_query->message->message_id;
$text = $message->text;
$contact = $message->contact;
$contactid = $contact->user_id;
$contactuser = $contact->username;
$contactname = $contact->first_name;
$phonenumber = $contact->phone_number;
$messagereply = $message->reply_to_message->message_id;
$user = $message->from->username;
$userid = $update->callback_query->from->username;
$query = $update->inline_query->query;
$inlineid = $update->inline_query->from->id;
$messagereply = $message->reply_to_message->message_id;
$soat = date("H:i:s"); 
$sana = date('d-M Y');
$resultid = file_get_contents("scsmm.bot");
$ban = file_get_contents("scsmm/$chatid.ban");
$banid = file_get_contents("scsmm/$chat_id.ban");
$sabab = file_get_contents("scsmm/$chat_id.sabab");
$contact = file_get_contents("scsmm/$chatid.contact");
$minimalsumma = file_get_contents("scsmm/minimal.sum");
$sum = file_get_contents("scsmm/$chatid.pul");
$sumid = file_get_contents("scsmm/$chat_id.pul");
$jami = file_get_contents("scsmm/summa.text");
$referal = file_get_contents("scsmm/$chatid.referal");
$referalcallback = file_get_contents("scsmm/$chat_id.referal");
$pay = file_get_contents("scsmm/$chatid.pay");
$paynet = file_get_contents("scsmm/$chatid.paynet");
$click = file_get_contents("scsmm/$chatid.click");
$referalsum = file_get_contents("scsmm/referal.sum");
$turi = file_get_contents("number/turi.txt");
$raqam = file_get_contents("number/$cid.txt");
$kanal = file_get_contents("scsmm/kanal.txt");
$supportuser = file_get_contents("scsmm/supportuser.txt");
$valbot = file_get_contents("scsmm/valbot.txt");
$qollanma = file_get_contents("scsmm/qollanma.txt");
$holat = file_get_contents("scsmm/holat.txt");
$paytoken= file_get_contents("scsmm/paytoken.txt");
$par= file_get_contents("scsmm/par.txt");
$tolovtt = file_get_contents("scsmm/tolovtt.txt");
$paykamissiya = file_get_contents("scsmm/kamissiya.txt");

if(file_get_contents("scsmm/kamissiya.txt")){
}else{    file_put_contents("scsmm/kamissiya.txt","sumOut");
}
if(file_get_contents("scsmm/supportuser.txt")){
}else{    file_put_contents("scsmm/supportuser.txt","off");
}
if(file_get_contents("scsmm/minimal.sum")){
}else{    file_put_contents("scsmm/minimal.sum","2");
}
if(file_get_contents("scsmm/valbot.txt")){
}else{    file_put_contents("scsmm/valbot.txt","RUB");
}
if(file_get_contents("scsmm/$chatid.referal")){
}else{    file_put_contents("scsmm/$chatid.referal","0");
}
if(file_get_contents("scsmm/$chat_id.referal")){
}else{    file_put_contents("scsmm/$chat_id.referal","0");
}
if(file_get_contents("scsmm/summa.text")){
}else{    file_put_contents("scsmm/summa.text","0");
}
if(file_get_contents("scsmm/referal.sum")){
}else{    file_put_contents("scsmm/referal.sum","0");
}
if(file_get_contents("scsmm/$chatid.pul")){
}else{    file_put_contents("scsmm/$chatid.pul","0");
}
if(file_get_contents("scsmm/$chat_id.pul")){
}else{    file_put_contents("scsmm/$chat_id.pul","0");
}
if(file_get_contents("scsmm/$chat_id.sabab")){
}else{    file_put_contents("scsmm/$chat_id.sabab","Botdan faqat O'zbekiston fuqarolari foydalanishi mumkin!");
}
$step = file_get_contents("scsmmbot/$chatid.step");

mkdir("kanal");
mkdir("scsmm");
mkdir("scsmmbot");
  mkdir("number");
if(!is_dir("scsmm")){
  mkdir("scsmm");

}

$menu = json_encode([
"resize_keyboard"=>true,
    "keyboard"=>[
[["text"=>"♻️ Pul ishlash"],],
[["text"=>"💰 Hisobim"],["text"=>"📩 Murojaat uchun"],],
[["text"=>"📝 To'lovlar tarixi"],],
[["text"=>"📊 Hisobot"],["text"=>"🗒 Qo‘llanma"],],
]
]);

if($text){
if($holat == "❌"){
if($chatid == $admin){
}else{
scsmm('sendMessage',[
'chat_id'=>$chatid,
'text'=>"⛔️ <b>Bot vaqtinchalik o'chirilgan!</b>

<i>Birozdan so`ng qayta /start bosing.</i>",
'parse_mode'=>'html',
]);
exit();
}
}else{
}
}

if($callbackdata){
if($holat == "❌"){
if($chat_id == $admin){
}else{
scsmm('answerCallbackQuery',[
'callback_query_id'=>$id,
'text'=>"⛔️ Bot vaqtinchalik o'chirilgan!

Birozdan so`ng qayta /start bosing.",
'show_alert'=>true,
]);
exit();
}
}else{
}
}

$panel = json_encode([
"resize_keyboard"=>true,
    "keyboard"=>[
[["text"=>"📨 Xabarnoma"]],
[["text"=>"🛠 Sozlamalar"],["text"=>"💰 Hisob olib tashlash"],],
[["text"=>"💳 Hisob tekshirish"],["text"=>"💰 Hisob toʻldirish"],],
[["text"=>"👥 Referal narxini o'zgartirish"],["text"=>"📤 Minimal yechish"],],
[["text"=>"✅ Bandan olish"],["text"=>"🚫 Ban berish"],],
[["text"=>"⬅️ Ortga"],],
]
]);

$boshqarish = json_encode([
"resize_keyboard"=>true,
    "keyboard"=>[
[["text"=>"↩ ortga"],],
]
]);

$kanalmen = json_encode([
"resize_keyboard"=>true,
    "keyboard"=>[
[["text"=>"📤 Majburiy kanal"],["text"=>"📝 To'lovlar kanali"],],
[["text"=>"📩 Murojaat user"],["text"=>"🗒 Qo‘llanma matn"],],
[["text"=>"💱 Bot valyutasi"],["text"=>"🛠 Bot holati"],],
[["text"=>"📝 Payeer parametrlari"],],
[["text"=>"↩ ortga"],],
]
]);

$back = json_encode([
 "one_time_keyboard"=>true,
"resize_keyboard"=>true,
    "keyboard"=>[
[["text"=>"⬅️ Ortga"],],
]
]);


if(($step=="request_contact") and ($ban==false) and (isset($phonenumber))){
$phonenumber = str_replace("+","","$phonenumber");
if(joinchat($fromid)=="true"){
if((strlen($phonenumber)==12) and (stripos($phonenumber,"998")!==false)){
if($contactid==$chatid){
addstat($fromid);
if($user){
$username = "@$user";
}else{
$username = "$firstname";
}
if(file_exists("scsmm/".$fromid.".referalid")){
$referalid = file_get_contents("scsmm/".$fromid.".referalid"); 
$channel = file_get_contents("scsmm/".$fromid.".channel");
$conts = file_get_contents("scsmm/".$fromid.".login");
if($channel=="true" and $conts=="false"){
if(joinchat($referalid)=="true"){
file_put_contents("scsmm/".$fromid.".login","true");
scsmm("deleteMessage",[
"chat_id"=>$chat_id,
"message_id"=>$message_id,
]);
$user = file_get_contents("scsmm/".$referalid.".pul");
$referalsum = $referalsum / 1;
$user = $user + $referalsum;
file_put_contents("scsmm/".$referalid.".pul","$user");
$firstname = str_replace(["<",">","/"],["","",""],$firstname);
scsmm("sendMessage",[
"chat_id"=>$referalid,
"text"=>"<b>👏 Tabriklaymiz! Sizni referalingiz</b> <a href='tg://user?id=$fromid’>$firstname</a> <b>botimizdan ro’yxatdan o’tdi va sizga $referalsum-$valbot taqdim etildi.</b>",
"parse_mode"=>"html",
"reply_markup"=>$menu,
]);
}
}
}
$reply = scsmm("sendMessage",[
"chat_id"=>$fromid,
"text"=>"<b>Bosh menyu</b>",
"parse_mode"=>"html",
"reply_markup"=>$menu,
])->result->message_id;
scsmm("sendMessage",[
"chat_id"=>$fromid,
"text"=>"",
"parse_mode"=>"html",
"reply_to_message_id"=>$reply,
"disable_web_page_preview"=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"↗️ Doʻstlarga yuborish","switch_inline_query"=>$fromid],],
]
]),
]);
unlink("scsmmbot/$chatid.step");
file_put_contents("scsmm/$chatid.contact","$phonenumber");
}else{
  addstat($chatid);
  scsmm("sendMessage",[
    "chat_id"=>$chatid,
    "text"=>"<b>Faqat o'zingizni kontaktingizni yuboring:</b>",
    "parse_mode"=>"html",
    "reply_markup"=>json_encode([
      "resize_keyboard"=>true,
      "one_time_keyboard"=>true,
      "keyboard"=>[
        [["text"=>"📲 Telefon raqamni yuborish","request_contact"=>true],],
]
]),
]);
}
}else{
  banstat($chatid);
  scsmm("sendMessage",[
    "chat_id"=>$chatid,
    "text"=>"<b>Kechirasiz! Botdan faqat O'zbekiston fuqarolari foydalanishi mumkin!</b>",
    "parse_mode"=>"html",
    "reply_to_message_id"=>$messageid,
    "reply_markup"=>json_encode([
    "remove_keyboard"=>true,
    ]),
  ]);
unlink("scsmmbot/$chatid.step");
file_put_contents("scsmm/$chatid.ban","ban");
}
}
}

if($text=="/admin" and $chatid==$admin){
typing($chatid);
scsmm('sendMessage',[
"chat_id"=>$chatid,
"text"=>"<b>Salom, Siz bot administratorisiz. Kerakli boʻlimni tanlang:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}

if($text=="↩ ortga" and $chatid==$admin){
typing($chatid);
scsmm('sendMessage',[
"chat_id"=>$chatid,
"text"=>"Panel",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}


if($text=="🛠 Sozlamalar" and $chatid==$admin){
typing($chatid);
scsmm('sendMessage',[
"chat_id"=>$chatid,
"text"=>"<b>Kerakli boʻlimni tanlang:</b>",
"parse_mode"=>"html",
"reply_markup"=>$kanalmen,
]);
}
if($text == "📨 Xabarnoma" and $chatid==$admin){
scsmm('SendMessage',[
'chat_id'=>$chatid,
'text'=>"<b>Yuboriladigan xabar turini tanlang;</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"Oddiy xabar",'callback_data'=>"send"],['text'=>"Forward xabar",'callback_data'=>"forsend"]],
[['text'=>"Foydalanuvchiga xabar",'callback_data'=>"user"]],
]])
]);
}
if($text=="↩Back" and $chatid==$admin){
typing($chatid);
scsmm('sendMessage',[
"chat_id"=>$chatid,
"text"=>"<b>Kerakli boʻlimni tanlang:</b>",
"parse_mode"=>"html",
"reply_markup"=>$kanalmen,
]);
}
if($callbackdata == "user"){
scsmm('deleteMessage',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
]);
scsmm('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"<b>Foydalanuvchi iD raqamini kiriting:</b>",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("scsmmbot/$chat_id.step",'user');
}

if($callbackdata == "bekor"){
scsmm('deleteMessage',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
]);
unlink("scsmmbot/$chat_id.step");
scsmm('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"Bekor qilindi",
'parse_mode'=>'html',
'reply_markup'=>$menu,
]);
}
if($callbackdata == "qayt"){
scsmm('deleteMessage',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
]);
scsmm('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"Bekor qilindi",
'parse_mode'=>'html',
'reply_markup'=>$kanalmen,
]);
}

if($step == "user"){
if($text=="↩ ortga"){
unlink("scsmmbot/$chatid.step");
}else{
if($chatid == $admin){
if(is_numeric($text)=="true"){
file_put_contents("scsmmbot/xbr.txt",$text);
scsmm('SendMessage',[
'chat_id'=>$chatid,
'text'=>"<b>Xabaringizni kiriting:</b>",
'parse_mode'=>'html',
]);
file_put_contents("scsmmbot/$chatid.step",'xabar');
}else{
scsmm('SendMessage',[
'chat_id'=>$chatid,
'text'=>"<b>Faqat raqamlardan foydalaning!</b>",
'parse_mode'=>'html',
]);
}}}}

if($step == "xabar"){
if($text=="↩ ortga"){
unlink("scsmmbot/$chatid.step");
}else{
if($chatid == $admin){
    $saved=file_get_contents("scsmmbot/xbr.txt");
scsmm('SendMessage',[
'chat_id'=>$saved,
'text'=>"$text",
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
]);
scsmm('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Xabaringiz yuborildi ✅</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel,
]);
unlink("scsmmbot/$chatid.step");
unlink("scsmmbot/xbr.txt");
}}}

if($callbackdata == "send"){
scsmm('deleteMessage',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
]);
scsmm('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"*Xabaringizni kiriting:*",
'parse_mode'=>"markdown",
'reply_markup'=>$boshqarish
]);
file_put_contents("scsmmbot/$chat_id.step","users");
}
if($step=="users"){
if($chatid == $admin){
$lich = file_get_contents("scsmm.bot");
$lichka = explode("\n",$lich);
foreach($lichka as $lichkalar){
$okuser=scsmm("sendmessage",[
'chat_id'=>$lichkalar,
'text'=>$text,
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
]);
}}}
if($okuser){
scsmm("sendmessage",[
'chat_id'=>$admin,
'text'=>"<b>Hammaga yuborildi ✅</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel
]);
unlink("scsmmbot/$chatid.step");
}

if($callbackdata == "forsend"){
scsmm('deleteMessage',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
]);
scsmm('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"*Xabaringizni yuboring:*",
'parse_mode'=>"markdown",
'reply_markup'=>$boshqarish
]);
file_put_contents("scsmmbot/$chat_id.step","forusers");
}
if($step=="forusers"){
if($text=="↩ ortga"){
unlink("step/$chatid.step");
}else{
if($chatid == $admin){
$lich = file_get_contents("scsmm.bot");
$lichka = explode("\n",$lich);
foreach($lichka as $lichkalar){
$okforuser=scsmm("forwardMessage",[
'from_chat_id'=>$chatid,
'chat_id'=>$lichkalar,
'message_id'=>$messageid,
]);
}}}}
if($okforuser){
scsmm("sendmessage",[
'chat_id'=>$admin,
'text'=>"<b>Hammaga yuborildi ✅</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel
]);
unlink("scsmmbot/$chatid.step");
}

if($text == "🛠 Bot holati"){
if($chatid == $admin){
scsmm('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Hozirgi holat:</b> $holat",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"✅",'callback_data'=>"holat-✅"],['text'=>"❌",'callback_data'=>"holat-❌"]],
[['text'=>"Yopish",'callback_data'=>"qayt"]]
]
])
]);
}
}

if(mb_stripos($callbackdata, "holat-")!==false){
$ex = explode("-",$callbackdata);
$xolat = $ex[1];
file_put_contents("scsmm/holat.txt",$xolat);
scsmm('editMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"<b>🔎 Hozirgi holat:</b> $xolat",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"✅",'callback_data'=>"holat-✅"],['text'=>"❌",'callback_data'=>"holat-❌"]],
[['text'=>"Yopish",'callback_data'=>"qayt"]]
]
])
]);
}

if ($text == "📝 Payeer parametrlari" and $chatid == $admin) {
    if (empty($paytoken)) { // Token mavjudligini tekshirish
        scsmm('SendMessage', [
            'chat_id' => $chatid,
            'text' => "❌ <b>To'lov uchun token mavjud emas!</b>\n\n▶ Iltimos, tokenni kiriting:",
            'parse_mode' => 'html',
            'reply_markup' => json_encode([
                'inline_keyboard' => [
                    [['text' => "▶ Token kiritish", 'callback_data' => "uptoken"]],
                ]
            ])
        ]);
    } else {
        
          $sckurs = file_get_contents("https://scsmm.uz/pay/?key=$paytoken&action=kurs");
$kursData = json_decode($sckurs, true);
 if (!empty($kursData)) {
        // USD va RUB uchun qiymatlarni olish
        $usdKurs = isset($kursData['USD']) ? $kursData['USD'] : 'N/A';
        $rubKurs = isset($kursData['RUB']) ? $kursData['RUB'] : 'N/A';
 }


        // Token mavjud bo’lsa, balansni olish
        $response = file_get_contents("https://scsmm.uz/pay?key=$paytoken&action=balance");
        
        // JSON-ni dekodlash
        $balanceData = json_decode($response, true);

        // Balansni tekshirish va foydalanuvchiga xabar ko’rsatish
        if (isset($balanceData['balance']) && isset($balanceData['currency'])) {
            $balans = $balanceData['balance'];
            $valyuta = $balanceData['currency'];

            // Kamissiya holatini tekshirish
            if ($paykamissiya == "sum") {
                // Foydalanuvchiga matnni ko’rsatish
                scsmm('SendMessage', [
                    'chat_id' => $chatid,
                    'text' => "💰 <b>Hisobda: $balans $valyuta\n\nTo'lov kursi:\nUSD-$usdKurs\nRUB-$rubKurs\n\n🔑 <b>Joriy token:</b> $paytoken\n\nKamissiya kimdan olinadi: $paykamissiya (Foydalanuvchidan)</b>",
                    'parse_mode' => 'html',
                    'reply_markup' => json_encode([
                        'inline_keyboard' => [
                            [['text' => "♻ Token yangilash", 'callback_data' => "uptoken"]],
                            [['text' => "✅ Kamissiyani sozlash", 'callback_data' => "kamissiya"]],
                        ]
                    ])
                ]);
            } elseif ($paykamissiya == "sumOut") {
                // Admin uchun matnni ko’rsatish
                scsmm('SendMessage', [
                    'chat_id' => $chatid,
                    'text' => "💰 <b>Hisobda: $balans $valyuta\n\nTo'lov kursi:\nUSD-$usdKurs\nRUB-$rubKurs\n\n🔑 <b>Joriy token:</b> $paytoken\n\nKamissiya kimdan olinadi: $paykamissiya (Admin)</b>",
                    'parse_mode' => 'html',
                    'reply_markup' => json_encode([
                        'inline_keyboard' => [
                            [['text' => "♻ Token yangilash", 'callback_data' => "uptoken"]],
                            [['text' => "✅ Kamissiyani sozlash", 'callback_data' => "kamissiya"]],
                        ]
                    ])
                ]);
            } 
        } else {
            // Xatolik yuz berganda
            scsmm('SendMessage', [
                'chat_id' => $chatid,
                'text' => "⚠ <b>Balansni olishda xatolik yuz berdi.</b>\n\n▶ Iltimos, tokeningizni tekshiring yoki qayta urinib ko'ring.",
                'parse_mode' => 'html',
                'reply_markup' => json_encode([
                    'inline_keyboard' => [
                        [['text' => "♻ Token yangilash", 'callback_data' => "uptoken"]],
                    ]
                ])
            ]);
        }
    }
}

if($callbackdata == "kamissiya"){
scsmm('editMessagetext',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"To'lov uchun kammisiya 1.45% olinadi, ushbu kamisiyani o'z hisobingizdan to'laysizmi yokiy foydalanuvchi hisobidan olinsinmi ?\n\n Foydalanuvchi hisobidan olinsa ishlagan pullarini yechganda 1.45% ushlab qolinadi!",
'parse_mode'=>'html',
'reply_markup' => json_encode([
                    'inline_keyboard' => [
                        [['text' => "♻ O'z hisobimdan", 'callback_data' => "kammisiya-sumOut"]],
                         [['text' => "♻ Foydalanuvchi hisobidan", 'callback_data' => "kammisiya-sum"]],
                    ]
                ])
            ]);
}

if(mb_stripos($callbackdata, "kammisiya-")!==false){
$ex = explode("-",$callbackdata);
$kamis = $ex[1];
file_put_contents("scsmm/kamissiya.txt",$kamis);
scsmm('editMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"<b>✅ Saqlandi:</b>",
'parse_mode'=>'html',
]);
}

if($callbackdata == "uptoken"){
scsmm('editMessagetext',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"<b>To'lov uchun token kiriting!</b>\nTokenni @ScSMMBot dan (🆓 Provayder API) buyrug'ini berib olasiz!\nBarcha to'lovlaringiz @ScSMMBot dan yechiladi!\n\nDiqqat!!\nTo'lov uchun kammisiya 1.45% olinadi, ushbu kamisiyani o'z hisobingizdan to'laysizmi yokiy foydalanuvchi hisobidan olinsinmi ?\n\n Foydalanuvchi hisobidan olinsa ishlagan pullarini yechganda 1.45% undan ushlab qolinadi!",
'parse_mode'=>'html',
]);
 file_put_contents("scsmmbot/$chat_id.step","uptoken");
}

if($step=="uptoken" and $chatid==$admin){
    typing($chatid);
file_put_contents("scsmm/paytoken.txt","$text");  
         scsmm('sendmessage',[ 
         'chat_id'=>$chatid, 
         'text'=>"✅  $text-saqlandi", 
 ]); 
unlink("scsmmbot/$chatid.step");
}

if($text=="📝 To'lovlar kanali" and $chatid==$admin){
    $kanallar = file_get_contents("scsmm/tolovtt.txt");
    scsmm('sendmessage', [ 
        'chat_id' => $chatid, 
        'text' => "Hozirgi o'rnatilgan kanal:\n$kanallar", 
        'parse_mode' => 'markdown',
        'reply_markup' => json_encode([
            "resize_keyboard" => true,
            "keyboard" => [
                [["text" => "📝 Kanal o'zgartirish"]],
                [["text" => "↩Back"]]
            ]
        ])
    ]); 
}

if ($text == "📝 Kanal o'zgartirish" && $chatid == $admin) {
    scsmm('sendmessage', [ 
        'chat_id' => $chatid, 
        'text' => "Kanalni ulamasangiz bot to'lov tizizmlari ishlamaydi!\nKanal manzilini kiriting: Namuna - @your_channel_username", 
        'parse_mode' => 'markdown',
    ]); 
    stepbot($chatid, "kanal_add");
} 

if ($step == "kanal_add" && $chatid == $admin) {
    typing($chatid);
    if (mb_stripos($text, "@") !== false) {
        $kanal_username = ltrim($text, "@");

        $chat_info = file_get_contents("https://api.telegram.org/bot".scsmm."/getChat?chat_id=@$kanal_username");
        $chat_info = json_decode($chat_info, true);

        if ($chat_info['ok'] && isset($chat_info['result']['type'])) {
            $chat_type = $chat_info['result']['type'];

            if ($chat_type == 'channel' || $chat_type == 'supergroup') {
                $chat_member = file_get_contents("https://api.telegram.org/bot".scsmm."/getChatMember?chat_id=@$kanal_username&user_id=" . $bot_id);
                $chat_member = json_decode($chat_member, true);

                if ($chat_member['ok'] && ($chat_member['result']['status'] == 'administrator' || $chat_member['result']['status'] == 'creator')) {

                    scsmm('sendmessage', [
                        'chat_id' => $chatid,
                        'text' => "✅ Muvaffaqiyatli saqlandi!",
                    ]);
                    unlink("scsmmbot/$chatid.step");

                    if (empty($kanallar)) {
                        unlink("scsmm/tolovtt.txt");
                        file_put_contents("scsmm/tolovtt.txt", $text);
                    }

                    unlink("scsmmbot/$chatid.step");
                } else {
                    scsmm('sendmessage', [
                        'chat_id' => $chatid,
                        'text' => "⚠️ Xato: Bot ushbu kanal yoki guruhda admin emas. Iltimos, kanal yoki guruhni tekshiring.",
                    ]);
                }
            } else {
                scsmm('sendmessage', [
                    'chat_id' => $chatid,
                    'text' => "⚠️ Xato: Kiritilgan username kanal yoki guruh emas. Iltimos, to'g'ri username kiriting.",
                ]);
            }
        } else {
            scsmm('sendmessage', [
                'chat_id' => $chatid,
                'text' => "⚠️ Xato: Kiritilgan kanal yoki guruh mavjud emas. Iltimos, to'g'ri kanal yoki guruh nomini kiriting.",
            ]);
        }
    } else {
        scsmm('sendmessage', [
            'chat_id' => $chatid,
            'text' => "⚠️ Xato: Iltimos, kanal yoki guruh username'ini to'g'ri kiriting.",
        ]);
    }
}

if($text == "📤 Majburiy kanal"){
scsmm('SendMessage',[
'chat_id'=>$chatid,
'text'=>"<b>Majburiy obunalarni sozlash bo'limidasiz:</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"➕ Qo'shish",'callback_data'=>"qoshish"]],
[['text'=>"📑 Ro'yxat",'callback_data'=>"royxat"],['text'=>"🗑 O'chirish",'callback_data'=>"ochirish"]],
]])
]);
}

if($callbackdata == "qoshish"){
scsmm('deleteMessage',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
]);
scsmm('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"<b>Kanalingiz userini kiriting:

Namuna:</b> @ByKons",
'parse_mode'=>'html',
'reply_markup'=>$boshqarish,
]);
file_put_contents("scsmmbot/$chat_id.step","qo'shish");
}

if($step == "qo'shish"){
if($tx=="↩ ortga"){
unlink("scsmmbot/$chatid.step");
}else{
if($chatid == $admin){
if(isset($text)){
if(mb_stripos($text, "@")!==false){
if($kanal == null){
file_put_contents("scsmm/kanal.txt",$text);
scsmm('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>$text - kanal qo'shildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel
]);
unlink("scsmmbot/$chatid.step");
}else{
file_put_contents("scsmm/kanal.txt","$kanal\n$text");
scsmm('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>$text - kanal qo'shildi!</b>",
'parse_mode'=>'html',
'reply_markup'=>$panel
]);
unlink("scsmmbot/$chatid.step");
}}else{
scsmm('SendMessage',[
'chat_id'=>$admin,
'text'=>"<b>Kanalingiz useri yuboring:

Namuna:</b> @ByKons",
'parse_mode'=>'html',
]);
}}}}}

if($callbackdata == "ochirish"){
scsmm('deleteMessage',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
]);
scsmm('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"<b>Kanallar o'chirildi</b>",
'parse_mode'=>'html',
]);
unlink("scsmm/kanal.txt");
}

if($callbackdata == "royxat"){
$soni = substr_count($kanal,"@");
if($kanal == null){
scsmm('editMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"📂 <b>Kanallar ro'yxati bo'sh!</b>",
'parse_mode'=>'html',
]);
}else{
scsmm('editMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"<b>📢 Kanallar ro'yxati:</b>

$kanal

<b>Ulangan kanallar soni:</b> $soni ta",
'parse_mode'=>'html',
]);
}}

if($step=="2" and $chatid==$admin){
typing($chatid);
if($text = "$text") { 
file_put_contents("scsmm/kanal.txt","$text");  
         scsmm('sendmessage',[ 
         'chat_id'=>$chatid, 
         'text'=>"✅ Majburiy a'zo kanali o'zgardi", 
 ]); 
unlink("scsmmbot/$chatid.step");
} 
}

if($text=="📩 Murojaat user" and $chatid==$admin){
    $manzilm = file_get_contents("scsmm/supportuser.txt");
    scsmm('sendmessage',[ 
  'chat_id'=>$chatid, 
  'text'=>"Murojat etish uchun Manzillar:\n $manzilm", 
  'parse_mode'=>'markdown',
  'reply_markup'=>json_encode([
  "resize_keyboard"=>true,
    "keyboard"=>[
        [["text"=>"⬅ O`zgartirish"],],
[["text"=>"↩Back"],],
]])
  ]); 
  } 
if($text=="⬅ O`zgartirish" and $chatid==$admin){
    scsmm('sendmessage',[ 
  'chat_id'=>$chatid, 
  'text'=>"Murojaat etish uchun usernamengizni @ belgisisiz yuboring

           *Namuna:\nAmirovBekjan\n\nAmirovBekjanBot*\n\nMurojaatni yopib qoyish uchun { off } sozini kiriting.", 
  'parse_mode'=>'markdown',
  ]); 
stepbot($chatid,"00");
  } 

if($step=="00" and $chatid==$admin){
typing($chatid);
if($text = "$text") { 
file_put_contents("scsmm/supportuser.txt","$text");  
         scsmm('sendmessage',[ 
         'chat_id'=>$chatid, 
         'text'=>"✅  @$text-Saqlandi", 
 ]); 
unlink("scsmmbot/$chatid.step");
} 
}


if($text=="🗒 Qo‘llanma matn" and $chatid==$admin){
    $qollat = file_get_contents("scsmm/qollanma.txt");
    scsmm('sendmessage',[ 
  'chat_id'=>$chatid, 
  'text'=>"Matn:\n $qollat", 
  'parse_mode'=>'markdown',
  'reply_markup'=>json_encode([
  "resize_keyboard"=>true,
    "keyboard"=>[
        [["text"=>"🗒 O`zgartirish"],],
[["text"=>"↩Back"],],
]])
  ]); 
  } 
if($text=="🗒 O`zgartirish" and $chatid==$admin){
    scsmm('sendmessage',[ 
  'chat_id'=>$chatid, 
  'text'=>"*Qo`llanma uchun matn kiriting*", 
  'parse_mode'=>'markdown',
  ]); 
stepbot($chatid,"qollanma");
  } 

if($step=="qollanma" and $chatid==$admin){
typing($chatid);
if($text = "$text") { 
file_put_contents("scsmm/qollanma.txt","$text");  
         scsmm('sendmessage',[ 
         'chat_id'=>$chatid, 
         'text'=>"✅ Saqlandi", 
 ]); 
unlink("scsmmbot/$chatid.step");
} 
}

if($text=="💱 Bot valyutasi" and $chatid==$admin){
    $valbot = file_get_contents("scsmm/valbot.txt");
    scsmm('sendmessage',[ 
  'chat_id'=>$chatid, 
  'text'=>"Bot valyutasi: $valbot", 
  'parse_mode'=>'markdown',
  'reply_markup'=>json_encode([
  "resize_keyboard"=>true,
    "keyboard"=>[
        [["text"=>"💱 O`zgartirish"],],
[["text"=>"↩Back"],],
]])
  ]); 
  } 
if($text == "💱 O`zgartirish" and $chatid == $admin) {
    scsmm('sendmessage', [ 
        'chat_id' => $chatid, 
        'text' => "*Bot to'lov tizimi valyutasini tanlang*",
        'parse_mode' => 'markdown',
        'reply_markup' => json_encode([
            "inline_keyboard" => [
                [["text" => "USD", "callback_data" => "val-USD"]],
                [["text" => "RUB", "callback_data" => "val-RUB"]],
                [["text" => "↩ Back", "callback_data" => "qayt"]],
            ]
        ])
    ]); 
}

if(mb_stripos($callbackdata, "val-")!==false){
$ex = explode("-",$callbackdata);
$valyutaex = $ex[1];
file_put_contents("scsmm/valbot.txt",$valyutaex);
scsmm('editMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"<b>✅ Saqlandi:</b> $valyutaex",
'parse_mode'=>'html',
]);
}

if($text=="💳 Hisob tekshirish" and $chatid==$admin){
typing($chatid);
stepbot($chatid,"result");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchini ID raqamini kiriting:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}

if($step=="result" and $chatid==$admin){
typing($chatid);
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
$sum = file_get_contents("scsmm/$text.pul");
$referal = file_get_contents("scsmm/$text.referal");
$raqam = file_get_contents("scsmm/$text.contact");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchi hisobi:</b> <code>$sum</code>\n<b>Foydalanuvchi referali:</b> <code>$referal</code>\n<b>Foydalanuvchi raqami:</b> <code>$raqam</code>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
unlink("scsmmbot/$chatid.step");
}
}

if($text=="💰 Hisob olib tashlash" and $chatid==$admin){
typing($chatid);
stepbot($chatid,"coinm");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchi hisobini necha pul olmoqchisiz </b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}

if($step=="coinm" and $chatid==$admin){
typing($chatid);
file_put_contents("scsmm/$chatid.coinm",$text);
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
stepbot($chatid,"paym");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchi ID raqamini kiriting:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}
}
//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo

if($step=="paym" and $chatid==$admin){
typing($chatid);
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
$summa = file_get_contents("scsmm/$chatid.coinm");
$sum =  file_get_contents("scsmm/$text.pul");
$jami = $sum - $summa;
file_put_contents("scsmm/$text.pul","$jami");
scsmm("sendMessage",[
   "chat_id"=>$text,
          "text"=>"💰 Hisobingiz: $summa olib tashlandi!\nHozirgi hisobingiz: $jami",
]);
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchi balansidan $text-olib tashlandi!</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
unlink("scsmmbot/$chatid.step");
}
}

if($text=="💰 Hisob toʻldirish" and $chatid==$admin){
typing($chatid);
stepbot($chatid,"coin");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchi hisobini necha pulga toʻldirmoqchisiz:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}

if($step=="coin" and $chatid==$admin){
typing($chatid);
file_put_contents("scsmm/$chatid.coin",$text);
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
stepbot($chatid,"pay");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchi ID raqamini kiriting:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}
}

if($step=="pay" and $chatid==$admin){
typing($chatid);
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
$summa = file_get_contents("scsmm/$chatid.coin");
$sum =  file_get_contents("scsmm/$text.pul");
$jami = $sum + $summa;
file_put_contents("scsmm/$text.pul","$jami");
scsmm("sendMessage",[
   "chat_id"=>$text,
          "text"=>"💰 Hisobingiz: $summa $valbotga to'ldirildi!\nHozirgi hisobingiz: $jami",
]);
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchi balansi toʻldirildi!</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
unlink("scsmmbot/$chatid.step");
}
}


if($text=="👥 Referal narxini o'zgartirish" and $chatid==$admin){
    $mref = file_get_contents("scsmm/referal.sum");
    scsmm('sendmessage',[ 
  'chat_id'=>$chatid, 
  'text'=>"1-referal narxi:\n $mref-$valbot", 
  'parse_mode'=>'markdown',
  'reply_markup'=>json_encode([
  "resize_keyboard"=>true,
    "keyboard"=>[
        [["text"=>"👥 O`zgartirish"],],
[["text"=>"↩ ortga"],],
]])
  ]); 
  } 
if($text=="👥 O`zgartirish" and $chatid==$admin){
typing($chatid);
stepbot($chatid,"referal");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Referal narxini kiriting:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}

if($step=="referal" and $chatid==$admin){
typing($chatid);
if(is_numeric($text)){
file_put_contents("scsmm/referal.sum","$text");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Referal taklif qilish narxi: $text $valbotga o'zgardi!</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
unlink("scsmmbot/$chatid.step");
}else{
    scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"Raqamlardan foydalaning.",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}
}

if($text=="✅ Bandan olish" and $chatid==$admin){
stepbot($chatid,"unban");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchini ID raqamini kiriting:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}
//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
if($step=="unban" and $chatid==$admin){
unlink("scsmm/$text.ban");
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
scsmm("sendMessage",[
"chat_id"=>$chatid,
"text"=>"<a href='tg://user?id=$text’>Foydalanuvchi</a> <b>bandan olindi!</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
unlink("scsmmbot/$chatid.step");
}
}

if($text=="🚫 Ban berish" and $chatid==$admin){
stepbot($chatid,"sabab");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchini nima sababdan ban qilmoqchisiz:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}

if($step=="sabab" and $chatid==$admin){
file_put_contents("scsmm/$chatid.sabab","$text");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Foydalanuvchini ID raqamini kiriting:</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
stepbot($chatid,"ban");
}

if($step=="ban" and $chatid==$admin){
banstat($text);
$sabab = file_get_contents("scsmm/$chatid.sabab");
file_put_contents("scsmm/$text.sabab","$sabab");
file_put_contents("scsmm/$text.ban","ban");
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
scsmm("sendMessage",[
"chat_id"=>$chatid,
"text"=>"<a href='tg://user?id=$text’>Foydalanuvchi</a> <b>banlandi!</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
unlink("scsmmbot/$chatid.step");
scsmm("sendMessage",[
"chat_id"=>$text,
"text"=>"<b>Hurmatli foydalanuvchi!</b>\n<b>Siz botdan banlandingiz. Shuning uchun botni ishlata olmaysiz!</b>",
"parse_mode"=>"html",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"📃 Batafsil maʼlumot","callback_data"=>"sabab"],],
]
]),
]);
}
}
//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
if ($text == "📝 To'lovlar tarixi" && $ban == false) {
    if ((joinchat($fromid) == "true") && (phonenumber($fromid) == "true")) {
        if (!empty($tolovtt)) {
            // Kanal nomidan ’@’ belgisini olib tashlash
            $kanal_username1 = ltrim($tolovtt, "@");

            scsmm("sendMessage", [
                "chat_id" => $chatid,
                "text" => "<b>✅ Botimiz to'lovlar kanaliga obuna bo'lishingiz mumkin. </b>\n\n" .
                          "<i>Quyidagi kanal orqali to'lovlar tarixini kuzatib boring👇</i>\n\n" .
                          "@$kanal_username1",
                "parse_mode" => "html",
                "reply_to_message_id" => $mid,
                "reply_markup" => json_encode([
                    "inline_keyboard" => [
                        [["text" => "Kanalga kirish 🧾", "url" => "https://t.me/$kanal_username1"]],
                    ]
                ]),
            ]);
        } else {
            scsmm("sendMessage", [
                "chat_id" => $chatid,
                "text" => "<b>To'lov manitoringi bot adminstratori tomonidan o'chirilgan.</b>",
                "parse_mode" => "html",
            ]);
        }
    }
}


if($text=="📩 Murojaat uchun" and $ban==false){
if((joinchat($fromid)=="true") and (phonenumber($fromid)=="true") and ($ban==false))
if($supportuser != off){
scsmm("sendMessage",[
   "chat_id"=>$chatid,
   "text"=>"<b>Murojaat uchun: @$supportuser</b>",
"parse_mode"=>"html",
'reply_to_message_id'=>$mid,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"Murojaat etish","url"=>"https://t.me/$supportuser"],],
]
]),
]);
exit();
}else{
	scsmm("sendMessage",[
"chat_id"=>$chatid,
"text"=>"<b>Murojaat etish bot adminstratori tamonidan o`chirilgan.</b>",
"parse_mode"=>"html",
		]);
}
}

if($text=="📤 Minimal yechish" and $chatid==$admin){
    $mmin = file_get_contents("scsmm/minimal.sum");
    scsmm('sendmessage',[ 
  'chat_id'=>$chatid, 
  'text'=>"Minimal pul yechish narxi:\n $mmin-$valbot", 
  'parse_mode'=>'markdown',
  'reply_markup'=>json_encode([
  "resize_keyboard"=>true,
    "keyboard"=>[
        [["text"=>"📤 O`zgartirish"],],
[["text"=>"↩ ortga"],],
]])
  ]); 
  } 

if($text=="📤 O`zgartirish" and $chatid==$admin){
typing($chatid);
stepbot($chatid,"minimalsumma");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Minimal pul yechish narxini kiriting:\nEng kam to'lov summasi\nmin 2-RUB\nmin 0.1-USD</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
}
//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
if($step=="minimalsumma" and $chatid==$admin){
typing($chatid);
if($text=="📨 Xabarnoma" or $text=="🛠 Sozlamalar" or $text=="💰 Hisob olib tashlash" or $text=="💳 Hisob tekshirish" or $text=="✅ Bandan olish" or $text=="🚫 Ban berish" or $text=="💰 Hisob toʻldirish" or $text=="⬅️ Ortga" or $text=="👥 Referal narxini o'zgartirish" or $text=="📤 Minimal yechish" or $text=="📤 Majburiy kanal" or $text=="📝 To'lovlar kanali" or $text=="📩 Murojaat user" or $text=="🗒 Qo‘llanma matn" or $text=="💱 Bot valyutasi" or $text=="📝 To'lovlar tarix" or $text=="🛠 Bot holati" or $text=="📝 Payeer parametrlari" or $text=="↩ ortga" or $text=="📝  O`zgartirish"){
}else{
file_put_contents("scsmm/minimal.sum","$text");
scsmm("sendMessage",[
"chat_id"=>$admin,
"text"=>"<b>Minimal pul yechish narxi: $text $valbotga o'zgardi!</b>",
"parse_mode"=>"html",
"reply_markup"=>$panel,
]);
unlink("scsmmbot/$chatid.step");
}
}

if($callbackdata=="back" and $banid==false){
if((joinchat($from_id)=="true") and (phonenumber($from_id)=="true") and ($banid==false)){
scsmm("deleteMessage",[
"chat_id"=>$chat_id,
"message_id"=>$message_id,
]);
scsmm("sendMessage",[
"chat_id"=>$chat_id,
"text"=>"<b>Kerakli boʻlimni tanlang</b> 👇",
"parse_mode"=>"html",
"reply_markup"=>$menu,
]);
}
}

if($text=="♻️ Pul ishlash" and $ban==false){
if((joinchat($fromid)=="true") and (phonenumber($fromid)=="true") and ($ban==false)){
if($user){
$username = "@$user";
}else{
$username = "$firstname";
}
scsmm("sendMessage",[
    "chat_id"=>$chatid,
"photo"=>"",
    "text"=>"<b>Hurmatli $firstname botimizdan pul ishlash uchun pastdagi referal havolani do'stlaringizga ulashing va pul ishlang!\n\n1-referal $referalsum-$valbot</b>\n\n<i>Taklif havolangiz👇</i>\n\nhttps://t.me/$botname?start=$chatid",
"parse_mode"=>"html",
"disable_web_page_preview"=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"💰Pul ishlashni boshlash","switch_inline_query"=>$chatid],],
]
]),
]);
}
}

if($text=="💰 Hisobim" and $ban==false){
if((joinchat($fromid)=="true") and (phonenumber($fromid)=="true") and ($ban==false)){
scsmm("sendMessage",[
"chat_id"=>$chatid,
"photo"=>"",
"text"=>"<b>Sizning balansingiz:</b> $sum-<b>$valbot</b>
<b>🗣 Siz botga taklif qilgan a'zolar soni:</b> $referal-<b>ta</b>
<b>💵 Bot toʻlab bergan jami summa:</b> $jami-$valbot
<b>🎈 Pul yechib olish uchun minimal summa:</b> $minimalsumma-<b>$valbot</b>",
"parse_mode"=>"html",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"Pul yechish","callback_data"=>"production"],],
]
]),
]);
}
}


if($text=="⬅️ Ortga" and $ban==false){
if((joinchat($fromid)=="true") and (phonenumber($fromid)=="true") and ($ban==false)){
addstat($chatid);
scsmm("sendMessage",[
"chat_id"=>$chatid,
"text"=>"<b>Kerakli boʻlimni tanlang</b> 👇",
"parse_mode"=>"html",
"reply_markup"=>$menu,
]);
unlink("scsmmbot/$chatid.step");
unlink("scsmmbot/$chatid.step");
}
}

if((stripos($text,"/start")!==false) && ($ban==false)){
if((joinchat($fromid)=="true") and (phonenumber($fromid)=="true") and ($ban==false)){
addstat($fromid);
if($user){
$username = "@$user";
}else{
$username = "$firstname";
}
$reply = scsmm("sendMessage",[
"chat_id"=>$fromid,
"text"=>"<b>Bosh menyu</b>",
"parse_mode"=>"html",
"reply_markup"=>$menu,
])->result->message_id;
scsmm("sendMessage",[
"chat_id"=>$fromid,
"text"=>"",
"parse_mode"=>"html",
"reply_to_message_id"=>$reply,
"disable_web_page_preview"=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"↗️ Doʻstlarga yuborish","switch_inline_query"=>$fromid],],
]
]),
]);
}
}

//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
if((stripos($text,"/start")!==false) && ($ban==false)){
$public = explode("*",$text);
$refid = explode(" ",$text);
$refid = $refid[1];
if(strlen($refid)>0){
$idref = "scsmm/$refid.id";
$idrefs = file_get_contents($idref);
$userlar = file_get_contents("scsmm.bot");
$explode = explode("\n",$userlar);
if(!in_array($chatid,$explode)){
file_put_contents("scsmm.bot","\n".$chatid,FILE_APPEND);
}
if($refid==$chatid and $ban==false){
      scsmm("sendMessage",[
      "chat_id"=>$chatid,
      "text"=>"☝️ <b>Hurmatli foydalanuvchi!</b>\n<b>Botga o'zingizni taklif qila olmaysiz!</b>",
      "parse_mode"=>"html",
      "reply_to_message_id"=>$messageid,
      ]);
      }else{
    if((stripos($userlar,"$chatid")!==false) and ($ban==false)){
      scsmm("sendMessage",[
      "chat_id"=>$chatid,
      "text"=>"<b>Hurmatli foydalanuvchi!</b>\n<b>Siz referalingiz referal bo'la olmaysiz, agar ushbu holat yana takrorlansa, siz botdan blocklanishingiz mumkin!</b>",
"parse_mode"=>"html",
"reply_to_message_id"=>$messageid,
]);
}else{
$id = "$chatid\n";
$handle = fopen("$idref","a+");
fwrite($handle,$id);
fclose($handle);
file_put_contents("scsmm/$fromid.referalid","$refid");
file_put_contents("scsmm/$fromid.channel","false");
file_put_contents("scsmm/$fromid.login","false");
      scsmm("sendMessage",[
      "chat_id"=>$refid,
"text"=>"<b>👏 Tabriklaymiz! Siz referalingiz</b> <a href='tg://user?id=$chatid’>foydalanuvchi</a><b>ni botga taklif qildingiz!</b>\n<b>referalingiz kanalimizga a’zo bo’lmagunicha, biz sizga referal puli taqdim etmaymiz!</b>",
"parse_mode"=>"html",
]);
}
}
}
}

if($callbackdata=="result" and ($banid==false)){
    scsmm("deleteMessage",[
"chat_id"=>$chat_id,
"message_id"=>$message_id,
]);
addstat($from_id);
if((joinchat($from_id)=="true")  and ($banid==false)){
if(phonenumber($from_id)=="true"){
if($userid==true){
$result = "@$userid";
}else{
$result = "$first_name";
}
scsmm("deleteMessage",[
"chat_id"=>$from_id,
"message_id"=>$message_id,
]);
$reply = scsmm("sendMessage",[
"chat_id"=>$from_id,
"text"=>"<b>Bosh menyu</b>",
"parse_mode"=>"html",
"reply_markup"=>$menu,
])->result->message_id;
scsmm("sendMessage",[
    "chat_id"=>$from_id,
"photo"=>"",
    "caption"=>"",
"parse_mode"=>"html",
"reply_to_message_id"=>$reply,
"disable_web_page_preview"=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"↗️ Doʻstlarga yuborish","switch_inline_query"=>$from_id],],
]
]),
]);
}
$time =  microtime(true);
$random  = rand(999999,3456789);
usleep($random);
$current  = microtime(true)-$time;
usleep($current);
if($referalsum==true){
if(file_exists("scsmm/".$from_id.".referalid")){
$referalid = file_get_contents("scsmm/".$from_id.".referalid");
if(joinchat($referalid)=="true"){
$is_user = file_get_contents("scsmm/".$from_id.".channel");
$login = file_get_contents("scsmm/".$from_id.".login");
if($is_user=="false" and $login=="false"){
$minimal = $referalsum / 1;
$referal = file_get_contents("scsmm/".$referalid.".referal");
$referal = $referal + 1;
file_put_contents("scsmm/".$referalid.".referal",$referal);
file_put_contents("scsmm/".$from_id.".channel","true");
$firstname = str_replace(["<",">","/"],["","",""],$firstname);
scsmm("sendMessage",[
"chat_id"=>$referalid,
"text"=>"<b>👏 Tabriklaymiz! Sizning referalingiz</b> <a href='tg://user?id=".$from_id."’>".$first_name."</a> <b>kanallarga a’zo bo’ldi.</b>\n<b>referalingiz roʻyxatdan oʻtsa, sizga  ".$minimal." $valbot taqdim etiladi!</b>",
"parse_mode"=>"html",
"reply_markup"=>$menu,
]);
}
}
}
}
}else{
scsmm("answerCallbackQuery",[
"callback_query_id"=>$id,
"text"=>"Siz hali kanallarga aʼzo boʻlmadingiz!",
"show_alert"=>false,
]);
}
}


if($callbackdata=="production" and $banid==false){
if((joinchat($from_id)=="true") and (phonenumber($from_id)=="true") and ($banid==false)){
  if (!empty($tolovtt)) {
if($par != "OFF"){
    scsmm("deleteMessage",[
    "chat_id"=>$chat_id,
    "message_id"=>$message_id,
]);
 scsmm("sendMessage",[
    "chat_id"=>$chat_id,
          "text"=>"💰 <b>Sizning hisobingizda: $sumid-$valbot mavjud!</b>\n<b>Pulingizni yechib olish uchun hamyonni tanlang!</b>",
          "parse_mode"=>"html",
  "reply_markup"=>json_encode([
"inline_keyboard"=>[
[['text'=>"🅿 Payeer",'callback_data'=>"pay-Payeer"]]
]
]),
                  ]);
}else{
scsmm('answerCallbackQuery',[
'callback_query_id'=>$id,
'text'=>"To'lov tizimlari admin tarafidan o`chirilgan, iltimos keynroq qayta urunib ko`ing!",
'show_alert'=>true,
]);
}
}else{
scsmm('answerCallbackQuery',[
'callback_query_id'=>$id,
'text'=>"To'lov tizimlari topilmadi!",
'show_alert'=>true,
]);
}
}
}


if (mb_stripos($callbackdata, "pay-") !== false) {
    $ex = explode("-", $callbackdata);
    $wallet = $ex[1];
  if (!empty($tolovtt)) {
        if ($sumid >= $minimalsumma) {
            scsmm('deleteMessage', [
                'chat_id' => $chat_id,
                'message_id' => $message_id,
            ]);
            scsmm('SendMessage', [
                'chat_id' => $chat_id,
                'text' => "❗ $wallet-ga pulni yechib olish uchun $wallet raqamni kiriting.\n\nTo'lov raqamini to'liq kiriting, Namuna: P123456789",
                'parse_mode' => 'markdown',
                'reply_markup' => json_encode([
                    'resize_keyboard' => true,
                    'keyboard' => [
                        [['text' => "⬅️ Ortga"]],
                    ]
                ])
            ]);
            stepbot($chat_id, "wallet-$wallet");
        } else {
            $som = $minimalsumma - $sumid;
            scsmm('answerCallbackQuery', [
                'callback_query_id' => $id,
                'text' => "☝️ Sizning hisobingizda mablag yetarli emas!\nSizga yana mablag'ni yechib olish uchun $som $valbot kerak!\nSizning hisobingizda: $sumid $valbot mavjud!",
                'show_alert' => true,
            ]);
        }
    } else {
        scsmm('answerCallbackQuery', [
            'callback_query_id' => $id,
            'text' => "Toʻlov manitoringi kanali ulanmagan, ( bu holatda botdan pul yechish taqiqlanadi. )",
            'show_alert' => true,
        ]);
    }
}
//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
if (mb_stripos($step, "wallet-") !== false) {
    $ex = explode("-", $step);
    $wallet = $ex[1];
    if ($text == "⬅️ Ortga") {
        unlink("scsmmbot/$chatid.step");
    } else {
        // Raqamni P bilan boshlanishini tekshirish
        if (preg_match('/^P\d+$/', $text)) {
            scsmm('SendMessage', [
                'chat_id' => $chatid,
                'text' => "Qancha miqdorda pul yechib olmoqchisiz?",
                'parse_mode' => 'html',
                'reply_markup' => json_encode([
                    'resize_keyboard' => true,
                    'keyboard' => [
                        [['text' => "$sum"]],
                        [['text' => "⬅️ Ortga"]],
                    ]
                ])
            ]);
            file_put_contents("scsmmbot/$chatid.step", "miqdor-$wallet-$text");
        } else {
            // Xatolik xabari ko’rsatish
            scsmm('SendMessage', [
                'chat_id' => $chatid,
                'text' => "❌ To'lov raqami noto'g'ri kiritildi!\n\nTo'g'ri namuna: <code>P123456789</code>",
                'parse_mode' => 'html',
                'reply_markup' => json_encode([
                    'resize_keyboard' => true,
                    'keyboard' => [
                        [['text' => "⬅️ Ortga"]],
                    ]
                ])
            ]);
        }
    }
}


if (mb_stripos($step, "miqdor-") !== false) {
    $ex = explode("-", $step);
    $wallet = $ex[1];
    $num = $ex[2];
    $hisob = file_get_contents("scsmm/$chatid.pul");

    if ($text == "⬅️ Ortga") {
        unlink("scsmmbot/$chatid.step");
    } else {
        if ($text >= $minimalsumma) {
            if ($hisob >= $text) {
                $raqam = file_get_contents("scsmm/$chatid.raqam");
                $referal = file_get_contents("scsmm/$chatid.referal");

                // Pul o’tkazish so’rovini yuborish
                $url = "https://scsmm.uz/pay/?key=$paytoken&payment_type=payeer&action=transfer&account=$num&currency=$valbot&transfer_type=$paykamissiya&amount=$text&comment=$botname";
                $response = file_get_contents($url); // Bu yerda so’rov yuboriladi

                // JSON-ni dekodlash
                $responseData = json_decode($response, true);

                // Agar muvaffaqiyatli o’tkazilsa
                if (isset($responseData['status']) && $responseData['status'] == 'success') {
                    scsmm("sendMessage", [
                        "chat_id" => "$tolovtt",
                        "text" => "*💳 Foydalanuvchi puli toʻlab berildi!*\n\n👤 *Foydalanuvchi*: [$chatid](tg://user?id=$chatid)\n🔢 *Raqami:* `*******`\n*👥 Taklif qilgan aʼzolari:* `$referal`\n💰 *To’lov miqdori:* `$text` *$valbot*\n\n✅ *Muvaffaqiyatli oʻtkazildi!*\n🌐By: @$botname",
                        "parse_mode" => "markdown",
                    ]);
                    $jami = file_get_contents("scsmm/summa.text");
                    $jami1 = $jami + $text;
                    file_put_contents("scsmm/summa.text","$jami1");
                    $hisob = file_get_contents("scsmm/$chatid.pul");
                    $puts = $hisob - $text;
                    file_put_contents("scsmm/$chatid.pul","$puts");
                    scsmm("sendMessage", [
                        "chat_id" => $chatid,
                        "text" => "<b><b>Pul bir necha soniyada hisobingizga tushadi! 🎉</b>\n\n💸 Sizning pulingiz muvaffaqiyatli o'tkazildi va tez orada hisobingizda aks etadi. Pul ishlash jarayonini davom ettiring va yanada ko'proq daromad toping!</b>",
                        "parse_mode" => "html",
                        "reply_markup"=>$menu,
                    ]);
                    
                } else {
                    // Xatolik yuz beradigan holat
                    scsmm('SendMessage', [
                        'chat_id' => $chatid,
                        'text' => "⚠ <b>Xatolik yuz berdi: Pul o'tkazishda muammo bor. Iltimos, qayta urinib ko'ring.</b>",
                        'parse_mode' => 'html',
                    ]);
                    scsmm('SendMessage', [
                        'chat_id' => $admin,
                        'text' => "⚠ <b>Foydalanuvchi pul yechisda muammo bo'ldi: $response</b>",
                        'parse_mode' => 'html',
                    ]);
                }

                unlink("scsmmbot/$chatid.step");
            } else {
                scsmm('SendMessage', [
                    'chat_id' => $chatid,
                    'text' => "💵 Sizning hisobingizda siz yechib olmoqchi bo'lgan pul mavjud emas!\nSiz faqat $hisob $valbot-pulni yechib olishingiz mumkin!",
                    'parse_mode' => 'html',
                ]);
            }
        } else {
            scsmm('SendMessage', [
                'chat_id' => $chatid,
                'text' => "Minimal pul yechish miqdori: $minimalsumma-$valbot",
                'parse_mode' => 'html',
            ]);
        }
    }
}


//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
if(mb_stripos($query,"$inlineid")!==false){
$user = $update->inline_query->from->username;
$firstname = $update->inline_query->from->first_name;
if($user){
$username = "@$user";
}else{
$username = "$firstname";
}
scsmm("answerInlineQuery",[
"inline_query_id"=>$update->inline_query->id,
"cache_time"=>1,
"results"=>json_encode([[
"type"=>"article",
"id"=>base64_encode(1),
"title"=>"🎈 Unikal havola-taklifnoma",
"description"=>"$username doʻstingizdan unikal havola-taklifnoma",
"thumb_url"=>"https://yearling-truck.000webhostapp.com/demo/download.png",
"input_message_content"=>[
"disable_web_page_preview"=>true,
"parse_mode"=>"html",
"message_text"=>"✅ <b>$botname tizimining rasmiy boti</b> 🤖\n\n🎈 $username do'stingizdan unikal havola-taklifnoma.\n\n👇 Boshlash uchun bosing:\nhttps://t.me/$botname?start=$inlineid"],
"reply_markup"=>[
"inline_keyboard"=>[
[["text"=>"🚀 Boshlash","url"=> "https://t.me/$botname?start=$inlineid"],],
]]
],
])
]);
}

if($text=="🗒 Qo‘llanma" and $ban==false){
if((joinchat($fromid)=="true") and (phonenumber($fromid)=="true") and ($ban==false)){
    if($qollanma != null){
scsmm("sendMessage",[
   "chat_id"=>$chatid,
   "text"=>"<b>$qollanma</b>",
"parse_mode"=>"html",
'reply_to_message_id'=>$mid,
]);
exit();
}else{
	scsmm("sendMessage",[
"chat_id"=>$chatid,
"text"=>"<b>Qo`llanma bot adminstratori tamonidan kiritilmagan.</b>",
"parse_mode"=>"html",
		]);
}
}
}


if($text=="📊 Hisobot" and $ban==false){
if((joinchat($fromid)=="true") and (phonenumber($fromid)=="true") and ($ban==false)){
$userlar = file_get_contents("scsmm.bot");
$count = substr_count($userlar,"\n");
$member = count(file("scsmm.bot"))-1;
$banusers = file_get_contents("scsmm.ban");
$bancount = substr_count($userlar,"\n");
$banmember = count(file("scsmm.ban"))-1;
    scsmm("sendMessage",[
"chat_id"=>$chatid,
"text"=>"<b>Botdagi a‘zolar soni:</b> $member-<b>ta</b>
<b>Botdan ban olganlar:</b> $banmember-<b>ta</b>
<b>Bot to'lab bergan jami summa:</b> $jami-<b>$valbot</b>",
"parse_mode"=>"html",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"♻️ Yangilash","callback_data"=>"upgrade"],],
]
]),
]);
}
}

if($callbackdata=="upgrade" and $banid==false){
if((joinchat($from_id)=="true") and (phonenumber($from_id)=="true") and ($banid==false)){
    	
$referal = file_get_contents("scsmm/$chat_id.referal");
$userlar = file_get_contents("scsmm.bot");
$count = substr_count($userlar,"\n");
$member = count(file("scsmm.bot"))-1;
$banusers = file_get_contents("scsmm.ban");
$bancount = substr_count($userlar,"\n");
$banmember = count(file("scsmm.ban"))-1;
scsmm("editMessageText",[
"chat_id"=>$chat_id,
"message_id"=>$message_id,
"text"=>"<b>Botimiz a'zolari soni:</b> <code>$member</code>\n<b>Qora roʻyxatdagi a'zolar soni:</b> <code>$banmember</code>\n<b>Siz botga taklif qilgan aʼzolar soni:</b> <code>$referal</code>\n\n$sana-$soat",
"parse_mode"=>"html",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"♻️ Yangilash","callback_data"=>"upgrade"],],
]
]),
]);
scsmm("answerCallbackQuery",[
"callback_query_id"=>$id,
"text"=>"Botimiz a'zolari soni: $member\nQora roʻyxatdagi a'zolar soni: $banmember\nSiz botga taklif qilgan aʼzolar soni: $referal\n\n$sana-$soat",
"show_alert"=>true,
]);
}
}

if($ban==true){
scsmm("deleteMessage",[
"chat_id"=>$chatid,
"message_id"=>$messageid,
]);
scsmm("sendMessage",[
"chat_id"=>$chatid,
"text"=>"<b>Hurmatli foydalanuvchi!</b>\n<b>Siz botdan banlangansiz. Shuning uchun botni ishlata olmaysiz!</b>",
"parse_mode"=>"html",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"📃 Batafsil maʼlumot","callback_data"=>"sabab"],],
]
]),
]);
}
//Kod Amirov Bekjan tomonidan tarqatildi, kodni maker botlar uchun ishlatsaxam boladi. Telegram: @AmirovBekjanInfo
if($banid==true){
scsmm("deleteMessage",[
"chat_id"=>$chat_id,
"message_id"=>$message_id,
]);
scsmm("sendMessage",[
"chat_id"=>$chat_id,
"text"=>"<b>Hurmatli foydalanuvchi!</b>\n<b>Siz botdan banlangansiz. Shuning uchun botni ishlata olmaysiz!</b>",
"parse_mode"=>"html",
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[["text"=>"📃 Batafsil maʼlumot","callback_data"=>"sabab"],],
]
]),
]);
}

if($callbackdata=="sabab"){
scsmm("answerCallbackQuery",[
"callback_query_id"=>$id,
"text"=>$sabab,
"show_alert"=>true,
]);
}
