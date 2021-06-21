<?php
defined('BASEPATH') or exit('No direct script access allowed');

class Auth extends CI_Controller
{
    public function index()
    {
        $this->load->view('templates/auth_header');
        $this->load->view('auth/login');
        $this->load->view('templates/auth_footer');
    }

    public function registration()
    {

        $this->load->view('templates/auth_header');
        $this->load->view('auth/registration');
        $this->load->view('templates/auth_footer');
    }

    public function registrasi()
    {
        $this->load->view('templates/auth_header');
        $this->load->view('auth/registration');
        $this->load->view('templates/auth_footer');
    }

    public function simpan()
    {
        if ($this->input->post('action') == 'simpan_reg') {
            # code...
            $data = [
                'id' => $this->input->post(''),
                'nama' => $this->input->post('nama'),
                'nama_p' => $this->input->post('nama_p'),
                'email' => $this->input->post('email'),
                'password' => $this->input->post('pass')
            ];

            $this->MRegis->simpan_registrasi($data);
        }
    }

    public function simpan_barang()
    {
    }
}
