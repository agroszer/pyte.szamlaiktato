<?php

/**
 * Onlineszamlazo.hu minta webhook kliens program.
 *
 * define('SHARED_SECRET', '__AUTOMATIC_FILLED_32_CHAR__'); // Beállítások / Külső kapcsolatok / WEBHOOK adatküldés
 * require_once("webhook/client.class.php");
 * $webhook = new \webhook\client();
 * $webhook->setSetting( array( 'conn' => array ( 'sharedSecret' => SHARED_SECRET ) ) );
 * $webhook->start();
 * $data = $webhook->getData();
 *
 */

namespace webhook;

class client
{
	private $version	= 1.01;
	private $data		= NULL;
	private $headers	= NULL;
	private $dataState	= 'OK'; // ERR
	private $hashAlgo	= 'sha384'; // ha megvaltoztatjuk itt is meg kell: X-Webhook-Hmac-sha384
	private $config		= NULL;

	public function __construct() {}

	/*
	 * Set configuration
	 */
	public function setSetting( array $config )
	{
		$this->config = $config;
	}

	/*
	 * Start process.
	 */
	public function start()
	{
		$this->readData();

		$this->verifyData();

		$this->response();
	}

	/*
	 * Return with received data.
	 */
	public function getData() : array 
	{
		return $this->data;
	}

	/*
	 * Return with received headers.
	 */
	public function getHeaders() : array 
	{
		return $this->headers;
	}

	/**
	 * Accept the data from stream
	 */
	private function readData()
	{
		$data = file_get_contents("php://input");
		if($data != ""){
			$data = json_decode($data, true);
			if(is_array($data)){
				$this->data = $data;
			}
		}
	}

	/**
	 * Verify request
	 */
	private function verifyData()
	{
		$this->dataState = 'ERR';

		$headers = array();
		foreach( getallheaders() as $k => $val ){
			if( preg_match("#X-Webhook-.*#i", $k) ){
				$headers[ strtolower($k) ] = $val;
			}
		}
		$this->headers = $headers;

		$sign = $this->getSignature( $this->config['conn']['sharedSecret'], json_encode($this->data) );
		if( $sign == $headers['x-webhook-hmac-sha384'] ){
			$this->dataState = 'OK';
		}

		/*
		$this->logger( $sign );
		$this->logger( $headers[ 'x-webhook-hmac-sha384' ] );
		 */
	}

	private function getSignature( string $sharedSecret, string $data ) : string
	{
		return base64_encode(hash_hmac($this->hashAlgo, $data, trim($sharedSecret), true));
	}

	/**
	 * Send request
	 */
	private function response()
	{
		// required headers to response
		header("Access-Control-Allow-Origin: *");
		header("Content-Type: application/json; charset=UTF-8");
		header("Access-Control-Allow-Methods: POST");
		header("Access-Control-Max-Age: 3600");
		header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

		http_response_code(503);
		if( $this->dataState == 'OK' ){
			http_response_code(200);
		}

		$request = array (
			'state' => 'RESPONSE',
			'param' => $this->data,
		);

		echo json_encode($request);
	}

	private function logger( string $msg ) : void {
		$file = __DIR__ . "/" . __CLASS__ . ".log";
		file_put_contents($file, $msg . "\n", FILE_APPEND | LOCK_EX);
	}
}

