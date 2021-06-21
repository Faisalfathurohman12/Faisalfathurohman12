<?php

defined('BASEPATH') or exit('No direct script access allowed');

class MRegis extends CI_Model
{
    public function simpan_registrasi($data)

    {

        if ($this->db->insert('pengguna', $data)) {
            # code...
            echo 'berhasil';
        } else {
            echo 'gagal';
        }
    }
}

/* End of file MRegis.php */
