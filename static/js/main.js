new ClipboardJS('.clipboard');
let bitcoinCp = new ClipboardJS('#bitcoinAddress', {
    text: function () {
        return '1AmdLAaG9YtnMb51n5jCZZ1jV58cNEL7is'
    }
});
let ethereumCp = new ClipboardJS('#ethereumAddress', {
    text: function () {
        return '0x76fB3d644A937849d7b660BeDf0558C5e1d85230'
    }
});
const $secretKey = $('#secretKey');
const $generateBtn = $('#generate');
const $copyBitcoin = $('#bitcoinAddress');
const $copyEthereum = $('#ethereumAddress');
const possible = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)';
let popupStack = {
    position: 'left center',
    target: '.icon.input',
    on: 'click',
    title: 'Click on Generate!',
    content: '',
    transition: 'pulse',
    duration: '200',
    hoverable: !0,
    exclusive: !0,
};

$secretKey.popup(popupStack);
$generateBtn.popup({
    position: 'left center',
    target: '.icon.input',
    on: 'click',
    title: 'Copied!',
    content: 'Just paste it to settings.',
    transition: 'pulse',
    duration: '200',
    hoverable: !0,
    exclusive: !0,
});
$generateBtn.click(function () {
    getNew();
});

bitcoinCp.on('success', function (e) {
    $copyBitcoin.html('Copied!');
    $copyBitcoin.addClass('positive');

    setTimeout(function () {
        $copyBitcoin.html('Copy');
        $copyBitcoin.removeClass('positive')
    }, 1500);
    e.clearSelection()
});
ethereumCp.on('success', function (e) {
    $copyEthereum.html('Copied!');
    $copyEthereum.addClass('positive');

    setTimeout(function () {
        $copyEthereum.html('Copy');
        $copyEthereum.removeClass('positive')
    }, 1500);
    e.clearSelection()
});

$('h1.ui.header').transition('pulse');
$('#dark-mode').checkbox({
    onChecked: function () {
        $('.light').toggleClass('dark').removeClass('light');
        $('#github-logo').attr('src', 'static/images/gitHub-mark-light.svg');
    },
    onUnchecked: function () {
        $('.dark').toggleClass('light').removeClass('dark');
        $('#github-logo').attr('src', 'static/images/gitHub-mark-dark.svg');
    }
});
$('#policy').click(function () {
    $('#policyModal').modal('show').modal({
        transition: 'pulse',
        closable: !0,
    })
});
$('#why').click(function () {
    $('#whyModal').modal('show').modal({
        transition: 'pulse',
        closable: !0,
    })
});
$('#bestpractice').click(function () {
    $('#bestpracticeModal').modal('show').modal({
        transition: 'pulse',
        closable: !0
    })
});
$('#supportme').popup({
    target: '#supportme',
    on: 'click',
    transition: 'pulse',
    duration: '200',
    hoverable: !0,
});

function generateNew() {
    let newSecretKey = '';

    for (let i = 0; i < 50; i++) {
        newSecretKey += possible.charAt(Math.floor(Math.random() * possible.length));
    }

    return newSecretKey;
}

function getNew() {
    $generateBtn.addClass('loading');

    let newSecretKey = generateNew();

    popupStack.title = 'Copied!';
    popupStack.content = 'Just paste it to settings.';

    $secretKey.val(newSecretKey);
    $secretKey.popup(popupStack);

    new ClipboardJS('.clipboard', {
        text: function () {
            return newSecretKey
        }
    });

    setTimeout(function () {
        $generateBtn.removeClass('loading')
    }, 200)
}
