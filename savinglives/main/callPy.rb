require "/Users/manavdutta/verboice-api-ruby/lib/verboice.rb"
def returnContact()
  verboice = Verboice.new("http://verboice.instedd.org","manavbiodutta@yahoo.com", "sparta300", "Mattie")
  queueCall = verboice.call("3689007575")
  id = queueCall["call_id"]
  state = queueCall["state"]
end

puts returnContact()
