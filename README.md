# Password Generator

Bu uygulama, kullanıcıların belirli kriterlere göre rastgele parolalar oluşturmasına olanak tanır. Hem bir web arayüzü hem de bir API üzerinden kullanılabilir.

## Özellikler

- Parola uzunluğunu belirleyebilme
- Büyük harfler, küçük harfler, rakamlar ve özel karakterler içerecek şekilde parolalar oluşturabilme
- Web arayüzü üzerinden parola oluşturma
- REST API üzerinden parola oluşturma

## Kurulum

1. Bu projeyi yerel makinenize klonlayın:
    ```sh
    git clone https://github.com/fzozyurt/password_generator.git
    cd password_generator
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

3. Uygulamayı başlatın:
    ```sh
    flask run
    ```

## Kullanım

### Web Arayüzü

Web arayüzünü kullanarak parola oluşturmak için tarayıcınızda `http://127.0.0.1:5000/` adresine gidin. Parola kriterlerini seçin ve "Generate Password" butonuna tıklayın.

### API

API üzerinden parola oluşturmak için aşağıdaki örnekteki gibi bir POST isteği gönderin:

- URL: `http://127.0.0.1:5000/`
- Metod: POST
- İçerik Türü: JSON
- Gönderilecek Veri:
    ```json
    {
      "length": 12,
      "uppercase": false,
      "lowercase": false,
      "digits": false,
      "special": true
    }
    ```

- Örnek cURL komutu:
    ```sh
    curl -X POST http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{
      "length": 8,
      "uppercase": true,
      "lowercase": true,
      "digits": false,
      "special": true
    }'
    ```

- Yanıt:
    ```json
    {
      "password": "Unw=_E:@"
    }
    ```