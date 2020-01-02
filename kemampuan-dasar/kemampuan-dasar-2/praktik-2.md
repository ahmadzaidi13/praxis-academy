#Team collaboration with GitHub#

##Menambahkan Anggota##
untuk kolaborasi dalam organisasi atau dengan kelompok tertentu dengan GitHub dapat dilakukan pada halaman https://github.com/settings/organizations. Setelah itu anggota dapat diundang dengan invite person. Anggota memiliki 3 jenis adminstrative authorization: 
-pull only
-push and pull
-push, pull & administrative

anggota dapat menggunakan <git clone> untuk mengkopi isi repo, <git pull> puntuk menyatukan dan mengambil isi repo dan <git push> untuk update repo

##Pull Request##
Dua model dari pull request:
1. Fork & Pull Model - digunakan dalam repo yang kita tidak memiliki push akses
2. Share repository model - digunakan dalam repository privat di mana user memiliki akses push

saat ada user lain yang melakukan fork maka akan terlihat pada pojok kanan atas di status fork

##Bug Tracking##
Bug Tracking merupakan fitur di mana user atau user lain dapat mencari bug dalam program, menambahkan fitur baru atau to do list hal yang harus dilakukan. 
Fitur pada bagian ini:
1. Labels: label berwarna untuk setial kategori untuk menyaring isu
2. Milestones: berisi kategori hal yang telah dilakukan dengan isu tertentu pada program.
3. Search: kolom pencarian di kanan atas dashboard untuk mencari isu.
4. Assignment: menugaskan isu terntentu kepada anggota yang nantinya akan tercatat dalam milestones.
5. Auto-close: saat message dengan <Fixes/Fixed or Close/Closes/Closed #[issue-number]> menandakan bahwa issue tersebut telah diperbaiki.
6. Mention issue dengan menggunakan <#nama-isu> contoh <#1> akan memention isu nomer 1

##Analytics##
Analytics merupakan alat yang digunakan untuk memberikan insight pada repo, tools ini berupa: Graphs dan Network

Graphs menyediakan detil seperti
- Contributor: siapa saja kontributor dalam repo dan berapa banyak baris kode yang telah mereka tambahkan atau hapus.
- Commit Activity: Memberikan informasi tentang aktivitas commit yang dilakukan
- Code Frequency: berapa banyak kode yang di commit selama project berlangsung.
- Punchcard: Memberikan informasi aktivitas commit per hari

Network menyediakan informasi commit dari setiap kotributor dalam bentuk satu grafik.


##Project Management##
GiHub dapat dihubungkan dengan Trello dan Pivotal Tracker untuk mendapat fitur fitur lain.
Trello pada dasarnya adalah tool management dengan visual yang lebih sederhana. Fitur otomatisasi merupakan fitur unggulan dari Trello.
Pivotal merupakan tool lain dengan narasi mirip seperti sebuah sosial media di mana developer dapat langsung berinteraksi dengan perubahan dan progress dari proyek yang dijalankan.


##Continuous Integration##
Continuous Integration (CI) merupakan alat untuk memeriksa apakah devepoler telah megecek kode dan error. Hal ini berguna untuk mempercepat perbaikan kode.

##Code Review#
Code review merupakan fitur untuk mereview kode yang ada dalam project. Beberapa fitur yang ada yaitu:
1. Compare branches/tags/SHA
2. Compare without whitespace
3. Diff
4. Patch
5. Line Linking

##Documenting##
Documenting berfungsi untuk menjelaskan bagian-bagian dalam project. Penjelasan dapat dilakukan dengan beberapa cara berikut:
1. Github Wiki
	Github wiki berada pada sub menu di headbar dan dapat di masukkan sebagai submodule pada kode.
2. Hubot
	Hubot merupakan chat bot yang dapat digunakan tidak hanya pada GitHub namun juga pada Skype, IRC, Gtalk dan lainnya.

