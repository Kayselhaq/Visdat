#import library yang dibutuhkan
import streamlit as st

#text element
st.header("Ini header") # untuk membuat header
st.subheader("Ini sub header") # untuk membuat sub header
st.text("ini text biasa tanpa format") # untuk membuat text polos tanpa format
st.markdown("**ini text bold** dan *ini text italic*")# markdown untuk memformat text tebal/miring
st.markdown("""
- ini baris 1
1. ini baris 2
* ini baris 3
""") # multi baris
st.caption("ini caption") # text kecil dibawah element
st.title("Ini Judul")

# coba mandiri

st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1 : Text Element")
st.markdown("""
1. ROZA KURNIAWAN NUR WAKID - 0110222124
2. PRAMANA RAHMANSAH PUTRA - 0110122051
3. IMAD HASAN AQIL - 0110221166
""")

# bagian 2: menampilkan rumus latex
st.header("Displaying LaTex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumus kuadrat binominal

# bagian 3: menampilkan kode program
st.header("Displaying Code")
st.subheader("Python Code")

# simpan ke variable
code = '''
def hello():
    print("Hello, Streamlit!)
'''

# st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
public class GFG {
    public static void main(String arg){
        System.out.printIn("Hello World!);
    }
}
""", language='java')
# fungsi st.code() bisa digunakan untuk bahasa pemograman lain seperti java, javasricpt, c++, html, dll

st.subheader("JavaScript Code")
st.code("""
<script>
try {
    addalert("welcome guest!); // kesalahan ketik (addalaert) sengaja dibuat untuk menimbulkan error    
}
catch(err) {
    document.getElementById("demo"), innerHTML = err.message; // menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language='javascript')
# kode ini menunjukkan contoh bagaimana menangani error (exception) di javascript
# hasilnya tidak di jalan kan di streamlit, tapi ditampilkan sebagai contoh kode